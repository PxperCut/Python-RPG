import random
import time
import cutie
import utils
from utils import clear_terminal, typewrite_text, textspeed, name, playervals,clamp
import dictionary
from dictionary import sayatk, sayimage
import Inventory
from Inventory import openinv,storeitem

playervals.specials=[
    "Pass",
    "Bash"
]

# VALID SPECIALS V
#playervals.specials=[
#    "Pass",
#    "Focus",
#    "Bash",
#    "Charge",
#    "Cure",
#    "Guard Break",
#    "Bite",
#    "Gamble"
#]

#VALID ATTAKS:
#'Nothing'
#'Slash'
#'Poison'
#'Decay'
#'Heal Self'
#'Buff'

#VALID ATTRIBUTES:
#'Spikey'

EnemyDataList = {
    "Gremlin": {
        "Attacks": ["Slash", "Nothing", "Heal Self"],
        "Attributes": ["None"],
        "Description": "A tiny Gremlin. He's a cutie pie, generally harmless.",
        "SOUL": 5
    },
    "Eyeball": {
        "Attacks": ["Slash", "Decay", "Buff"],
        "Attributes": ["None"],
        "Description": "A sentient eyeball. It's always watching.",
        "SOUL": 8
    },
    "Slime": {
        "Attacks": ["Slash", "Strong Slash", "Poison"],
        "Attributes": ["None"],
        "Description": "A disgusting mess of goop and bones.",
        "SOUL": 10
    },
    "Turtine": {
        "Attacks": ["Slash", "Heal Self", "Buff"],
        "Attributes": ["Spikey"],
        "Description": "What appears to be an odd turtle. Although it's shell is covered in crude spikes.",
        "SOUL": 10
    },
    "Rotter": {
        "Attacks": ["Slash", "Decay", "Poison"],
        "Attributes": ["None"],
        "Description": "A shambling zombie-like creature.",
        "SOUL": 8
    },
    "Grub": {
        "Attacks": ["Slash", "Strong Slash", "Heal Self", "Nothing"],
        "Attributes": ["None"],
        "Description": "A large lava-esq monster. It constantly searches for food.",
        "SOUL": 9
    },
    "Hero": {
        "Attacks": ["Slash", "Strong Slash", "Decay", "Buff"],
        "Attributes": ["None"],
        "Description": "A Hero who can do no wrong.",
        "SOUL": 20
    }
}

def Battle(id, eHP, eATK, eDF):
    buff_active=False
    invalidatks = []
    eMAXHP = eHP
    Charge=False

    EnemyData = EnemyDataList[id]
    Enemy_Attributes = EnemyData["Attributes"]
    turn = True
    applied_status = False

    def useatk(Special, Enemy_Attributes, eHP, Charge):
        clear_terminal()
        miss = 10
        sayimage("Reg", id)
        atkdmg = 0

        if Special == "Default":
            typewrite_text("I attacked!", textspeed)
            time.sleep(0.5)
            miss = random.randint(1, 10)
            atkdmg = random.randint(playervals.atk, playervals.atk + 1)-eDF
            atkdmg=clamp(atkdmg,1,atkdmg)
        else:
            typewrite_text(f"\033[1mI used\033[0m {Special.upper()}", textspeed)
            time.sleep(.5)
            if Special == "Bash":
                if playervals.SP >= 2:
                    playervals.SP -= 2
                    atkdmg = playervals.atk+3-eDF
                else:
                    typewrite_text("\nI don't have enough SP!", textspeed)
                    time.sleep(0.5)

            elif Special == "Gamble":
                if playervals.SP >= 5:
                    playervals.SP -= 5

                    if random.randint(1,2) == 1:
                        playervals.hp = int(playervals.MAXHP * 0.7)
                        healed=playervals.hp=clamp(playervals.hp,playervals.hp,playervals.MAXHP)
                        playervals.hp=healed
                        if playervals.hp==playervals.MAXHP:
                            typewrite_text("\n\033[1mMy HP was maxxed out!\033[0m", textspeed)
                        else:
                            typewrite_text(f"\n\033[1m(I recovered {healed} HP)\033[0m", textspeed)
                        time.sleep(0.6)
                    else:
                        playervals.hp-=2
                        typewrite_text("Something churns in my stomach.\n(I lost 2 health.)",textspeed)
                    time.sleep(0.6)
                else:
                    typewrite_text("\nbut I didn’t have enough SP!", textspeed)
                    time.sleep(0.5)

            elif Special == "Cure":
                if playervals.SP >= 3:
                    playervals.SP -= 3
                    if playervals.inflictions:
                        for status, _ in list(playervals.inflictions):
                            playervals.inflictions.remove((status, _))
                            typewrite_text(f"\n\033[1mI am no longer suffering from {status}.\033[0m", textspeed)
                            if status in invalidatks:
                                invalidatks.remove(status)
                            time.sleep(0.6)
                    else:
                        print()
                        typewrite_text("\nI am already free of any ailments.", textspeed)
                        time.sleep(0.6)
                else:
                    typewrite_text("I don't have enough SP!", textspeed)
                    time.sleep(0.5)

            elif Special == "Focus":
                playervals.SP = min(playervals.SP + 2, playervals.MAXSP)
                print()
                typewrite_text("I focused and restored 2 SP.", textspeed)
                time.sleep(0.6)

            elif Special == "Swap":
                if playervals.SP>=3:
                    playervals.SP-=3
                    playervals.hp+=3
                    playervals.hp=clamp(playervals.hp,0,playervals.MAXHP)

                    if playervals.hp==playervals.MAXHP:
                        typewrite_text("\n\033[1mMy HP was maxxed out!\033[0m", textspeed)
                    else:
                        typewrite_text(f"\n\033[1m(I recovered 3 HP)\033[0m", textspeed)
                    time.sleep(1)

            elif Special == "Bite":
                if playervals.SP>=4:
                    playervals.SP-=4
                    eHP-=4
                    playervals.hp+=4
                    playervals.hp=clamp(playervals.hp,0,playervals.MAXHP)
                    typewrite_text(f"\nI stole 4 health from {id}!", textspeed)
                    if playervals.hp==playervals.MAXHP:
                        typewrite_text("\n\033[1mMy HP was maxxed out!\033[0m", textspeed)
                    else:
                        typewrite_text(f"\n\033[1m(I recovered 4 HP)\033[0m", textspeed)
                else:
                    typewrite_text("\nbut I didn't have enough SP!",textspeed)
                time.sleep(1)


            elif Special == "Guard Break":
                if playervals.SP >= 4:
                    playervals.SP-=4
                    print()
                    typewrite_text(f"{id}'s GUARD was broken!", textspeed)
                    atkdmg = playervals.atk+2
                else:
                    typewrite_text("\nbut I didn't have enough SP!",textspeed)
                    time.sleep(0.6)
            
            elif Special == "Charge":
                if playervals.SP >= 3:
                    playervals.SP-=3
                    print()
                    typewrite_text(f"My attack was increased for the next turn!", textspeed)
                    Charge=True
                    return eHP,Charge
                else:
                    typewrite_text("\nbut I didn't have enough SP!",textspeed)
                    time.sleep(0.6)
                
            elif Special == "Pass":
                typewrite_text("\nI passed my turn.",textspeed)

        if Enemy_Attributes:
            miss=0
            if "Spikey" in Enemy_Attributes and atkdmg>0:
                playervals.hp -= 1
                typewrite_text(f"\nAs I strike, {id} bristles its sharp spikes!\n(I lost 1 HP)",textspeed)
                time.sleep(0.6)
        if miss != 1 and atkdmg > 0:
            if Charge:
                typewrite_text("\nThe attack was CHARGED!",textspeed)
                atkdmg+=2
            clear_terminal()
            sayimage("Hurt", id)
            print(f"\033[1mI used\033[0m {Special.upper()}" if Special != "Default" else "I attacked!")
            typewrite_text(f"I dealt {atkdmg} damage!", textspeed)
            time.sleep(0.5)
            eHP -= atkdmg
        elif atkdmg > 0:
            print()
            typewrite_text("\033[1mbut it missed!\033[0m", textspeed)
            time.sleep(0.5)
        Charge=False
        return eHP,Charge

    while playervals.hp > 0 and eHP > 0:
        
        if turn and not applied_status:
            clear_terminal()
            if playervals.inflictions:
                new_inflictions = []
                for status, turns in playervals.inflictions:
                    clear_terminal()
                    if status == "Poison":
                        playervals.hp -= 1
                        sayimage("Reg", id)
                        typewrite_text("The poison festers in my skin (-1 HP)", textspeed)
                        time.sleep(1)

                    if status == "Decay":
                        if not playervals.SP<=0:
                            playervals.SP -= 1
                        sayimage("Reg", id)
                        typewrite_text("I feel myself Decaying. (-1 SP)", textspeed)
                        time.sleep(1)
                    turns -= 1
                    if turns > 0:
                        new_inflictions.append((status, turns))
                playervals.inflictions = new_inflictions

            applied_status = True


        if playervals.hp <= 0:
            clear_terminal()
            print("I have fallen in battle...")
            time.sleep(1.2)
            break

        clear_terminal()
        sayimage("Reg", id)
        print(f"\033[1m{id}\033[0m")
        print(f"\033[1mHP :\033[0m {eHP}/{eMAXHP}")
        print("--------------\n")
        print(f"\033[1m\033[33;1m{name}\033[0m\n\033[1mHP:\033[0m {playervals.hp}/{playervals.MAXHP}")
        print(f"\033[1mSP:\033[0m {playervals.SP}/{playervals.MAXSP}")
        if playervals.inflictions:
            print("\nInflictions:")
            for status, turns in playervals.inflictions:
                print(f"  • {status} ({turns} turn{'s' if turns != 1 else ''} left)")

        if turn:
            options = ["Fight",
                       "Special",
                       "Inventory",
                       "Check"]
            choice = cutie.select(options, selected_index=0, selected_prefix="\033[33;1m[*] \033[0m")

            if options[choice] == "Fight":
                eHP,Charge = useatk("Default", Enemy_Attributes, eHP, Charge)
                turn = False
                if eHP <= 0:
                    break

            elif options[choice] == "Special":
                while True:
                    clear_terminal()
                    sayimage("Reg", id)
                    print(f"\033[1m{id}\033[0m")
                    print(f"\033[1mHP :\033[0m {eHP}/{eMAXHP}")
                    print("--------------\n")
                    print(f"\033[1m\033[33;1m{name}\033[0m")
                    print(f"\033[1mHP:\033[0m {playervals.hp}/{playervals.MAXHP}")
                    print(f"\033[1mSP:\033[0m {playervals.SP}/{playervals.MAXSP}")
                    if playervals.inflictions:
                        print("\nInflictions:")
                        for status, turns in playervals.inflictions:
                            print(f"  • {status} ({turns} turn{'s' if turns != 1 else ''} left)")

                    special_options = playervals.specials + ["!desc"] + ["Back"]
                    clear_terminal()
                    choice = cutie.select(
                        special_options,
                        descriptions={
                            "Pass": "Pass your turn.",
                            "Focus": "Restores 2 SP (No cost)",
                            "Bash": "A heavy strike that deals extra damage (2 SP)",
                            "Swap": "Exchange 3 SP for 3 health. (3 SP)",
                            "Charge": "Do more damage on the following turn. (3 SP)",
                            "Cure": "Removes status effects (3 SP)",
                            "Guard Break": "A powerful strike, piercing through the eneimies defense. (4 SP)",
                            "Bite": "Steal 4 health from the enemy. (4 SP.)",
                            "Gamble": "A chance to restore 70 percent of your health. If it failure will result in damage. (5 SP)",
                        },
                        selected_prefix="\033[33;1m[*] \033[0m"
                    )
                    if special_options[choice] == "Back":
                        break
                    else:
                        eHP,Charge = useatk(special_options[choice], Enemy_Attributes, eHP, Charge)
                        turn = False
                        break

            elif options[choice] == "Inventory":
                if not "Fear" in playervals.inflictions:
                    selecteditem=openinv()
                    if selecteditem!=None:
                        clear_terminal()
                        turn=False
                        continue
                else:
                    clear_terminal()
                    typewrite_text("I am too afraid to use any items.",textspeed)
                    time.sleep(1)

            elif options[choice] == "Check":
                clear_terminal()
                print(f"\033[1m{id}:\033[0m")
                print(f"\"{EnemyData['Description']}\"")
                print(f"\n\033[1mHP:\033[0m {eMAXHP} \033[1mATK:\033[0m {eATK} \033[1mDF:\033[0m {eDF}")
                print(f"\033[1mAttributes:\033[0m {Enemy_Attributes}\n")
                cutie.select(["Back"], selected_prefix="\033[33;1m[*] \033[0m")

        if not turn and eHP > 0 and playervals.hp > 0:
            applied_status = False
            clear_terminal()
            sayimage("Reg", id)

            EnemyATK = random.choice([atk for atk in EnemyData["Attacks"] if atk not in invalidatks])
            typewrite_text(sayatk(EnemyATK, id), textspeed)
            time.sleep(0.4)

            miss = (random.randint(1, 10) == 1)
            atkdmg=0

            if EnemyATK == "Nothing":
                time.sleep(0.4)
            else:
                if not miss:
                    
                    if EnemyATK == "Slash":
                        atkdmg = random.randint(eATK, eATK + 2)
                        print()
                        typewrite_text(f"{id} dealt {atkdmg} damage.", textspeed)
                        time.sleep(0.4)

                    if EnemyATK == "Strong Slash":
                        atkdmg = random.randint(eATK, eATK + 3)
                        print()
                        typewrite_text(f"{id} dealt {atkdmg} damage.", textspeed)
                        time.sleep(0.4)

                    if EnemyATK == "Heal Self":
                        healed=random.randint(1,2)
                        eHP += healed
                        print()
                        typewrite_text(f"{id} regained {healed} health!", textspeed)
                        time.sleep(0.4)

                    elif EnemyATK == "Poison":
                        if not any(status == "Poison" for status, _ in playervals.inflictions):
                            playervals.inflictions.append(("Poison", 3))
                            invalidatks.append("Poison")
                            print()
                            typewrite_text("\033[1mI have been POISONED!\033[0m", textspeed)
                            time.sleep(0.4)

                    elif EnemyATK == "Decay":
                        if not any(status == "Decay" for status, _ in playervals.inflictions):
                            playervals.inflictions.append(("Decay", 3))
                            invalidatks.append("Decay")
                            print()
                            typewrite_text("\033[1mI have been inflicted with DECAY!\033[0m", textspeed)
                            time.sleep(0.4)

                    elif EnemyATK == "Buff":
                        buff_active=True
                        buff_duration=4
                        invalidatks.append("Buff")
                        print()
                        typewrite_text(f"\n\033[1mAll attacks from {id} are now buffed for {buff_duration - 1} turns!\033[0m", textspeed)
                        time.sleep(0.4)

                else:
                    print()
                    typewrite_text(f"\033[1m{id} missed!\033[0m", textspeed)
                    time.sleep(0.5)

            if buff_active==True:
                if buff_duration>0:
                    atkdmg+=2
                    buff_duration-=1
                else:
                    print()
                    typewrite_text(f"{id} is no longer buffed.",textspeed)
                    invalidatks.remove("Buff")
                    buff_active=False

            playervals.hp -= atkdmg
            turn = True

    clear_terminal()
    
    #end of battle
    if playervals.hp<=0:
        playervals.inflictions=[]
        typewrite_text("I've fallen in battle.",textspeed)
        time.sleep(1)
        clear_terminal()
        return "dead"
    else:
        SOUL=EnemyData["SOUL"]
        playervals.SOUL+=SOUL
        typewrite_text(f"I slayed the monster.\nI earned {SOUL} SOUL.",textspeed)
        time.sleep(1)
        clear_terminal()
        playervals.inflictions=[]
        return "defeated"