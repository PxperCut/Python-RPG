from utils import print_image_list,playervals,clamp,typewrite_text,textspeed,clear_terminal,apply_status
import time
import math
import random
import cutie

YELLOW = "\033[93m"
RESET = "\033[0m"

# VALID SPECIALS V
#    "Pass",
#    "Focus",
#    "Bash",
#    "Charge",
#    "Cure",
#    "Swap",
#    "Guard Break",
#    "Bite",
#    "Gamble"
#]

#   ---HP ITEMS---
#   "Sporecap" - Heals 1 HP 
#   "Sporeshroom" - Heals 2 HP
#   "Bandage" - Heals 3 HP
#   "Ghostmilk" - Heals 6 HP
#   "Buttery Pie" - Heals 8 HP
#   "Nightshade Oil" - Restores all HP, 10% chance to inflict Decay.
#   "Lichen Wrap" - Restores 25% of all HP.

#   ---SP, SPECIAL ITEMS---
#   "Small SP Potion" - Restores 2 SP
#   "SP Potion" - Restores 4 SP
#   "Lotus Flower" - Restores 6 SP
#   "Fern Leaf" - Restores 8 HP
#   "Blood Apple" - Cures all ailments, restores 2 SP.
#   "Nightshade Berry" - Damages 1 HP, restores 3 SP


#   ---COMBAT ITEMS---
#   "Bone Charm" - Charges your next attack.
#   "Sharp fang" - Deals 4 damage.
#   "Decay Bomb" - Removes 1 enemy DF.

# --STATUS EFFECTS--
#   "Decay" - Depletes 1 SP
#   "Poison" - Depletes 1 HP

def sayimage(imgdef,enemy):
    if imgdef=="Reg":

        if enemy == "Gremlin":
            print_image_list([
                "  /^ ^\ ",
                " ( o_o )",
                "  /   \ ",
                " v| - |v ",
                "   V V" 
            ])
        
        if enemy == "Eyeball":
            print_image_list([
                "    ___",
                "  /  |  \ ",
                " |-  O  -| ",
                "  \ _|_ /   " 
            ])
        
        if enemy == "Slime":
            print_image_list([
                "  _---_",
                " / 0 0 \ ",
                " |     | ",
                " /     \ ",
                " U-U-U-U  " 
            ])

        if enemy == "Rotter":
            print_image_list([
                " .----.",
                "( ,  , )",
                " /|  |\ ",
                " U|  |U",
                "  |||| ",
                "  U U"
            ])

        if enemy == "Turtine":
            print_image_list([
                "  + ^^^ .--.",
                " ^./ \./  * }",
                "<|_\_/__ /''",
                "/_/---\_\ "
            ])

        if enemy == "Grub":
            print_image_list([
                " ______",
                "(_|___/ \ ",
                "/ \_|___/_ ",
                "\__|_\\-__-/ "
            ])

    if imgdef=="Hurt":

        if enemy == "Gremlin":
            print_image_list([
                "  /^ ^\ ",
                " ( x_x )",
                "  /   \ ",
                " v| - |v ",
                "   V V" 
            ])

        if enemy == "Eyeball":
            print_image_list([
                "    ___",
                "  /  |  \ ",
                " |-  X  -| ",
                "  \ _|_ /   " 
            ])
        
        if enemy == "Slime":
            print_image_list([
                "  _---_",
                " / X X \ ",
                " | u   | ",
                " /   u \ ",
                " U-U-U-U  " 
            ])

        if enemy == "Turtine":
            print_image_list([
                "  + ^^^ .--.",
                " ^./ \./  X }",
                "<|_\_/__ /''",
                "/_/---\_\ "
            ])

        if enemy == "Rotter":
            print_image_list([
                "  .--.",
                " (x  x)",
                " /|  |\ ",
                " U|  |U",
                "  |||| ",
                "  U U"
            ])

        if enemy == "Grub":
            print_image_list([
                " ______",
                "(_|___/ \ ",
                "/ \_|___/_ ",
                "\__|_\\x__x/ "
            ])

def sayatk(atk,enemy):#enemy attacks

    if atk=="Slash":
        if enemy == "Gremlin":
            text="The Gremlin leaps forward to slash me with it's sharp claws."
        if enemy == "Eyeball":
            text="The Eyeball quivers and peels back to reveal a set of sharp teeth. It lunges forward to bite me."
        if enemy == "Slime":
            text="The Slime bounces from the floor to richochet off of me."
        if enemy == "Turtine":
            text="The Turtine whips around to swipe at me with its spikey tail."
        if enemy == "Rotter":
            text="The Rotter lurches forwards as it jabs its arm into me."
        if enemy == "Grub":
            text="The Grub lunges at me and sinks its teeth into me."
        if enemy == "Hero":
            text="The Hero lunges in a sudden arc and slashes me with his dulled blade."

    if atk=="Strong Slash":
        if enemy=="Slime":
            text="The Slime leaps forward to swipe at me with a surprising force."
        if enemy == "Grub":
            text="The Grub slams its head onto me, raking a powerful chomp."
        if enemy == "Hero":
            text="The Hero's thrusts his worn blade at me with great force and prescision."

    if atk=="Heal Self":
        if enemy == "Gremlin":
            text="The Gremlin takes a moment to regain its strength."
        if enemy == "Turtine":
            text="The Turtine hides in its shell to recover."
        if enemy == "Grub":
            text="The Grub curls into itself to ooze a foul mucus."

    elif atk=="Nothing":
        if enemy == "Gremlin":
            text="The Gremlin cowers in fear afraid of my presence. It is too fearful to attack me."
        if enemy == "Grub":
            text="The Grub seems distracted by the thought of food."

    elif atk=="Poison":
        if enemy == "Slime":
            text="The Slime splashes me with it's toxic goop. It burns my skin like acid."
        if enemy == "Rotter":
            text="The Rotter reeks of a stong odor of death."

    elif atk=="Decay":
        if enemy == "Eyeball":
            text="The eyeball stares at me. I feel something wither inside me, its gaze begins to rot me from within."
        if enemy == "Rotter":
            text="The Rotter exudes a naseous aura and I can feel my strength begin to wither."
        if enemy == "Hero":
            text="The Hero mutters something unintenliglble that sounds like worlds older than time itself.\nAt once I feel something eat away at my strength."
    elif atk=="Buff":
        if enemy == "Eyeball":
            text="The eyeball's pupil narrows in on me."
        if enemy == "Turtine":
            text="The Turtine sharpens its claws on its shell."
        if enemy == "Hero":
            text="The Hero's eyes flare with a yellow glow."
    return text

def inspectitem(item):#inspect items
    if item=="Sporecap":
        text="It's a tiny mushroom. Heals 1 HP."
    elif item=="Sporeshroom":
        text="It's a mushroom. Heals 2 HP."
    elif item=="Bandage":
        text="A hastily made bandage. Heals 3 HP."
    elif item=="Ghostmilk":
        text="Milk. But from ghosts probably. Heals 6 HP."
    elif item=="Buttery Pie":
        text="A lovingly made pie. Heals 8 HP."
    elif item=="Nightshade Oil":
        text="Oil from a Nightshade plant. Restores all HP with a 10 percent chance to inflict 'Decay'."
    elif item=="Lichen Wrap":
        text="A bandage worn by a Lichen. Restores 25 percent of all HP."

    elif item=="Small SP Potion":
        text="A tiny shimmering potion. Restores 2 SP."
    elif item=="SP Potion":
        text="A shimmering potion. Restores 4 SP."
    elif item=="Lotus Flower":
        text="A beautifully crafted flower. Restores 6 SP."
    elif item=="Fern Leaf":
        text="A leaf used in many herbal teas. Restores 8 SP."
    elif item=="Blood Apple":
        text="A dark red apple. Cures any ailments, restores 2 SP."
    elif item=="Nightshade Berry":
        text="Damages 1 HP, restores 3 SP."
    return text

def useitem(item):#use items
    Extra=None
    if item=="Sporecap":
        text="I consumed the Sporecap."
        hpdif=1
        spdif=0
        playervals.hp=clamp(playervals.hp+hpdif, 0, playervals.MAXHP)

    if item=="Sporeshroom":
        text="I consumed the Sporeshroom."
        hpdif=2
        spdif=0
        playervals.hp=clamp(playervals.hp+hpdif, 0, playervals.MAXHP)#deter the hp to change,0 ,maxrecoverable hp
    
    if item=="Bandage":
        text="I used the Bandange."
        hpdif=3
        spdif=0
        playervals.hp=clamp(playervals.hp+hpdif, 0, playervals.MAXHP)
    
    if item=="Ghostmilk":
        text="I drank the Ghostmilk."
        hpdif=6
        spdif=0
        playervals.hp=clamp(playervals.hp+hpdif, 0, playervals.MAXHP)
    
    if item=="Buttery Pie":
        text="I devoured the Buttery Pie."
        hpdif=8
        spdif=0
        playervals.hp=clamp(playervals.hp+hpdif, 0, playervals.MAXHP)
        time.sleep(1)
    if item=="Nightshade Oil":
        text="I used the Nightshade Oil."
        spdif=0
        if random.randint(1,1)==1:
            apply_status(playervals.inflictions,"Decay",3)
            hpdif=0
            Extra="Decay"
        else:
            hpdif=10
        playervals.hp=clamp(playervals.hp+hpdif, 0, playervals.MAXHP)

    if item == "Lichen Wrap":
        text = "I used the Lichen Wrap."
        missing_hp = playervals.MAXHP - playervals.hp
        hpdif = int(missing_hp * 0.75)
        spdif=0
        playervals.hp = clamp(playervals.hp + hpdif, 0, playervals.MAXHP)

    if item=="Small SP Potion":
        text="I drank the potion."
        hpdif=0
        spdif=2
        playervals.SP=clamp(playervals.SP+spdif, 0, playervals.MAXSP)
        
    if item=="SP Potion":
        text="I drank the potion."
        hpdif=0
        spdif=4
        playervals.SP=clamp(playervals.SP+spdif, 0, playervals.MAXSP)

    if item=="Lotus Flower":
        text="I used the Lotus Flower."
        hpdif=0
        spdif=6
        playervals.SP=clamp(playervals.SP+spdif, 0, playervals.MAXSP)

    if item=="Fern Leaf":
        text="I used the Fern Leaf."
        hpdif=0
        spdif=8
        playervals.SP=clamp(playervals.SP+spdif, 0, playervals.MAXSP)

    if item=="Blood Apple":
        text="I consumed the Blood Apple."
        hpdif=0
        spdif=3
        playervals.inflictions=[]
        Extra="Cure Ailments"
        playervals.SP=clamp(playervals.SP+spdif, 0, playervals.MAXSP)

    if item=="Nightshade Berry":
        text="I ate the Nightshade Berry."
        hpdif=-1
        spdif=3
        playervals.SP=clamp(playervals.SP+spdif, 0, playervals.MAXSP)

    return text,int(hpdif),int(spdif),Extra,
    


def sayitemroom(subtype,itemcount):
    if subtype == "Sporeshroom-Room":
        if itemcount > 0:
            text = (
                "As I step into the room, the air becomes thick with spores, "
                "\nA vast thickening of fungus covers the walls."
                "\n\nThere is a mushroom growing from a crevice on the floor."
                "\nIt glows faintly in the dark with an odd bluish hue."
            )
        else:
            text = "All that remains where the mushroom once grew is a dead and withered stem."

    elif subtype == "Podium-Room":
        if itemcount > 0:
            text = (
                "A podium lies in the middle of the room."
                "\na velvet flower, as well as a small glass potion rests there."
                "\nA plate inscribed on the front below reads 'From the kindness of my heart, these gifts may belong to you.'"
            )
        else:
            text = "The podium is now empty. What a kind thought, from a kind stranger."

    elif subtype == "Tree-Room":
        if itemcount > 0:
            text = (
                "An overgrown tree fills this room. Its roots cover the walls. I can barely see the top."
                "\nGetting a better look, I see a red apple hanging from the top."
            )
        else:
            text = "The tree looms over me, left with no more gifts to share."

    elif subtype == "Corpse-Room":
        if itemcount > 0:
            text = (
                "I am startled as I notice the decaying bones of a Lichen resting on the stone floor."
                "\nFunnily enough, he is still wrapped in tattered bandages. A sense of dread creeps through the air."
            )
        else:
            text = "The Lichen no longer wears his bandages.\nHe lays on the flooring, still as stone."

    elif subtype == "Shrine-Room":
        if itemcount > 0:
            text = "A shrine is placed on the floor in the middle of the room.\nA beautiful flower rests in front of it."
        else:
            text = "The shrine is left alone, with nothing to accompany it. It seems very lonely."

    elif subtype == "Berry-Room":
        if itemcount > 0:
            text = (
                "The room is tangled with thick, thorny vines that twist and crawl across every surface. "
                "Among the greenery ripe juicy berries hang temptingly."
            )
        else:
            text = (
                "The berries have all been picked, leaving the room eerily silent. "
                "The vibrant life here has suddenly gone dormant."
            )
    elif subtype == "Oil-Lamp-Room":
        if itemcount > 0:
            text = (
                "The room is dimly lit by a single flickering oil lamp."
                "\nOn a stone pedestal beneath it, I find a small vial."
                "\nThe air faintly reeks with something oddly sinister."
            )
        else:
            text = (
                "The lamp still flickers, but the pedestal is empty now."
                "\nA bitter smell lingers where the oil sat."
        )
    elif subtype == "Fern-Room":
        if itemcount > 0:
            text = (
                "This chamber is lush with ferns."
                "\nAt the center, a single glowing Fern Leaf sways gently."
            )
        else:
            text = (
                "The glow has faded. Only wilted fronds remain, they curl in on themselves."
            )

    elif subtype == "Empty-Room":
        text = ("The room is quiet and unremarkable.")

    return text


def saymonsterroom(subtype,defeated):
    while True:

        if subtype=="Gremlin Room":
            if not defeated:#if the enemy is not defeated...
                typewrite_text("Entering the room, I am startled as a pesky Gremlin pops out at me!",textspeed)
                time.sleep(1)
                from battle import Battle
                defeated = Battle("Gremlin", 8, 1, 0)#initiate battle
            else:#if the enemy IS defeated
                text=("The Gremlin lays on the floor, unconscious. I cant help but feel bad for him.")
                break

        if subtype=="Eyeball Room":
            if not defeated:#if the enemy is not defeated...
                typewrite_text("Entering the room, I am caught by an Eyeball's gaze!",textspeed)
                time.sleep(1)
                from battle import Battle
                defeated = Battle("Eyeball", 8, 2, 1)#initiate battle
            else:#if the enemy IS defeated
                text=("The Eyeball has exploded with a sudden pop. He won't be watching me anymore.")
                break

        if subtype=="Slime Room":
            if not defeated:#if the enemy is not defeated...
                typewrite_text("Entering the room, a ball of slime slithers from the cracks to reveal itself.",textspeed)
                time.sleep(1)
                from battle import Battle
                defeated = Battle("Slime", 10, 2, 1)#initiate battle
            else:#if the enemy IS defeated
                text=("The Slime has melted into a rather putrid puddle of goop.")
                break
        
        if subtype=="Turtine Room":
            if not defeated:#if the enemy is not defeated...
                typewrite_text("Entering the room, a Turtine peeks its head from its shell!",textspeed)
                time.sleep(1)
                from battle import Battle
                defeated = Battle("Turtine", 5, 1, 2)#initiate battle
            else:#if the enemy IS defeated
                text=("The Turtine's shell is now empty and it lays on the floor in an odd stillness.")
                break

        if subtype=="Rotter Room":
            if not defeated:#if the enemy is not defeated...
                typewrite_text("Entering the room, a Rotter shambles into view!",textspeed)
                time.sleep(1)
                from battle import Battle
                defeated = Battle("Rotter", 10, 4, 0)#initiate battle
            else:#if the enemy IS defeated
                text=("The Rotter has collapsed into a pile of dust and lies dormant.")
                break

        if subtype=="Grub Room":
            if not defeated:#if the enemy is not defeated...
                typewrite_text("Entering the room, I see a Grub slowly worm itself towards me!",textspeed)
                time.sleep(1)
                from battle import Battle
                defeated = Battle("Grub", 7, 3, 2)#initiate battle
            else:#if the enemy IS defeated
                text=("The Grub has curled into a ball, no longer able to disturb me.",textspeed)
                break

    return defeated,text

def entityroom(subtype,defeated):
            if subtype=="Merchant":
                typewrite_text("I can see a merchant who's set up shop. He looks at me and gestures towards his goods.",textspeed)
            if subtype=="Knight":
                typewrite_text("A knight is injured. He is leans heavily against the stone wall.",textspeed)
            if subtype=="Hero":
                if defeated==False:
                    typewrite_text("The room is eerily dark and reeks of blood and smoke."\
                "\nAgainst the far wall, I can hardly make out an battered man in rusted armor and muddy clothes." \
                "\nHis sword lays broken at his side. A tattered banner lays on his lap. It is unclear whether he is mourning or protecting it.",textspeed)
                else:
                    typewrite_text("The Hero has fallen to the floor. His cape has flipped upside on him, obscuring his face.",textspeed)

items = {
    "Sporeshroom": {"name": "Sporeshroom", "desc": "Restores 2 HP.\nCosts 5 SOUL.","cost":5},
    "Sporecap": {"name": "Sporecap", "desc": "Restores 1 HP.\nCosts 2 SOUL.","cost":2}, 
    "Bandage": {"name": "Bandage", "desc": "Restores 3 HP.\nCosts 4 SOUL.","cost":4},
    "Ghostmilk": {"name": "Ghostmilk", "desc": "Restores 6 HP.\nCosts 8 SOUL.","cost":8},
    "Buttery Pie": {"name": "Buttery Pie", "desc": "Restores 8 HP.\nCosts 12 SOUL.","cost":12},
    "Lichen Wrap": {"name": "Lichen Wrap", "desc": "Restores 25 percent of all HP.\nCosts 10 SOUL.","cost":10},
    "Nightshade Oil": {"name": "Nightshade Oil", "desc": "Restores all HP, 10 percent chance to inflict Decay.\nCosts 15 SOUL.","cost":15},

    "SP Potion": {"name": "SP Potion", "desc": "Restores 4 SP.\nCosts 4 SOUL.","cost":4},
    "Lotus Flower": {"name": "Lotus Flower", "desc": "Restores 6 SP.\nCosts 8 SOUL.","cost":8}, 
    "Blood Apple": {"name": "Blood Apple", "desc": "Cures all ailments, restores 2 SP.\nCosts 8 SOUL.","cost":8},
    "Nightshade Berry": {"name": "Nightshade Berry", "desc": "Damages 3 HP, restores 5 SP\nCosts 8 SOUL.","cost":8}, 
    "Fern Leaf": {"name": "Fern Leaf", "desc": "Restores 8 SP.\nCosts 10 SOUL.","cost":10}
}

def shop(char):
    while True:
        clear_terminal()
        print("\033[1m---SHOP---")
        
        if char == "Merchant":
            shop_items = [
                items["SP Potion"]["name"],
                items["Sporeshroom"]["name"]
                ]

        shop_items += ["!space", "Back"]
        print("\n\033[1mSOUL:\033[0m", playervals.SOUL)
        choice_index = cutie.select(shop_items, selected_prefix="\033[33;1m[*] \033[0m")
        choice = shop_items[choice_index]
        if choice == "Back":
            break
        elif choice == "!space":
            continue
        elif choice in items:
            item = items[choice]
            while True:
                clear_terminal()
                print(f"\033[1m{item['name']}\033[0m\n")
                print(item["desc"])
                options = ["Purchase", "Back"]
                print("\n\033[1mSOUL:\033[0m", playervals.SOUL)
                sub_choice_index = cutie.select(options, selected_prefix="\033[33;1m[*] \033[0m")
                sub_choice = options[sub_choice_index]

                if sub_choice == "Purchase":
                    clear_terminal()
                    if playervals.SOUL>=item["cost"]:
                        clear_terminal()
                        playervals.SOUL-=item["cost"]
                        typewrite_text(f"\nYou purchased {item['name']}.",textspeed)
                        from Inventory import storeitem
                        storeitem(item['name'])                    
                        time.sleep(1)
                        break
                    else:
                        typewrite_text("I don't have enough SOUL to afford that item.",textspeed)
                else:
                    break



def interactwentity(entity,defeated):
    while True:
        clear_terminal()

        if entity=="Merchant":
            typewrite_text("The Merchant looks up from his wares and his eyes slowly travel up to meet mine.",textspeed)
            print()
            choice = cutie.select([
                "Why are you here?",
                "Who are you?",
                "Your shop?",
                "!space",
                "Nevermind."],
                selected_prefix="\033[33;1m[*] \033[0m")
            clear_terminal()
            if choice==0:
                typewrite_text("The merchant only smiles and points towards his shop.",textspeed)
            elif choice==1:
                typewrite_text("The merchant does not have a reply.\nHe gestures towards his goods again.",textspeed)
            elif choice==2:
                shop(entity)
            elif choice==4:#back
                typewrite_text("The merchant smiles at you and waves his hand to give a shaky goodbye.",textspeed)
                time.sleep(1)
                break

        if entity=="Knight":
            typewrite_text("The Knight weakly lifts his head to look at you."\
            "\nAt last, he speaks, his teeth clenched. "\
            "\n'I'm fine on my own. What do you want?'",textspeed)
            print()
            choice = cutie.select([
                "Are you alright?",
                "Who are you?",
                "!space",
                "Nevermind."],
                selected_prefix="\033[33;1m[*] \033[0m")
            clear_terminal()
            if choice==0:
                typewrite_text("The Knight lets out a long sarcastic chuckle before grimmacing." \
                "\n'What do you think kid? I'm bleeding out over here. Stupid Rotter pounced on me, busted right through my armor.'",textspeed)
                time.sleep(.5)
                typewrite_text("\nHe coughs. 'I'll be alright I don't need your pity.'",textspeed)
            elif choice==1:
                typewrite_text("'Well, from what I can tell I'm just like you.'" \
                "\nHe scoffs." \
                f"\n'Stupid. Thought I could save the {YELLOW}MOON{RESET} all by myself. Trust me kid, pack your things and leave while you still can, you dont even stand a chance against a god.",textspeed)
            elif choice==2:
                shop(entity)
            elif choice==3:#back
                typewrite_text("The knight nods in your direction as you leave." \
                "\n'May luck walk beside you. you're going to need every bit of it that you can find.'",textspeed)
                time.sleep(1)
                break

        if entity=="Stranger":
            typewrite_text("The man chuckles as you approach him before coughing weakly."\
            "\n'Tell me, do you still believe in heroes?'",textspeed)
            print()
            choice = cutie.select([
                "I do.",
                "Not anymore.",
                "What happened to you?",
                "!space",
                "Nevermind."],
                selected_prefix="\033[33;1m[*] \033[0m")
            clear_terminal()
            if choice==0:
                typewrite_text("The man speaks.\n'That's a nice thought. Hold onto it while you can. Got that?'",textspeed)
            elif choice==1:
                typewrite_text("He nods slowly. "\
                "\n'The world is a cruel place. Everything breaks eventually. People most of all." \
                "\nJust remember, even if the world forgets you, even if you are not a hero, your descisions still matter." \
                "\n..." \
                "\nI really thought I could be one.'",textspeed)
            elif choice==2:
                typewrite_text(f"The man begins,"\
                f"\n'A voice spoke to me. It told me I could be the one to take back our {YELLOW}MOON{RESET}."\
                "\n..And for a while I believed it.'",textspeed)
                print()
                subchoice=cutie.select(["I was told the same thing.","Why did you stop?"],selected_prefix="\033[33;1m[*] \033[0m")
                if subchoice==0:
                    clear_terminal()
                    typewrite_text("The man stares at you bewildered." \
                    "\nThen it's already found another..." \
                    "\nI can't let you be used. Not like I was." \
                    "\nHe slowly rises and pulls out a broken sword from beneath his tattered cloak." \
                    "\nI'm sorry, but this ends for you here.",textspeed)
                    time.sleep(1)
                    from battle import Battle
                    defeated=Battle("Hero", 15, 2, 0)#initiate battle
                    if defeated=="dead": 
                        return "dead"
                    if defeated=="defeated":
                        return defeated
                elif subchoice==1:
                    clear_terminal()
                    typewrite_text("The man turns away and stares into the distance solemly." \
                    "\n'It lied to me.'" \
                    "\nHe cups his hands." \
                    "\n'It promised I would be the one to fix everything. To save us." \
                    f"\n'It just wants the damn {YELLOW}MOON{RESET} for itself.'" \
                    "\n That voice is no saivor. It's just as much of a thief as the first.",textspeed)
                    time.sleep(1)
            elif choice==4:#back
                typewrite_text("The man lets you be." \
                "\n'Don't be fooled, friend. I hope you find what you are looking for.''",textspeed)
                time.sleep(1)
                break

def deathmessage():    
    import main 
    from main import name
    name = f"{YELLOW}{name}{RESET}"
    #--DEATH MESSAGES---
    if playervals.deathcount == 0:
        typewrite_text("Oh dear...\nIt seems you've met a horrible demise. ",textspeed)
        time.sleep(.5)
        typewrite_text(f"That is quite alright.\nAfter all, your story does not end here. I cannot allow you to die {name}.\nNot without our {YELLOW}MOON{RESET}.",textspeed)
        time.sleep(.5)
        clear_terminal()
        typewrite_text(f"You are weak. You deserve another chance."
                       f"\nI will grant you strength and you will rise again.",textspeed)
        clear_terminal()
        typewrite_text(f"This time do not falter. The {YELLOW}MOON{RESET} awaits you, {name}.\nAnd so do I.",textspeed)
        time.sleep(1)
        playervals.specials.append("Focus")
        typewrite_text("\n(You learned FOCUS)",textspeed)
        time.sleep(1)

    elif playervals.deathcount == 1:
        typewrite_text("I see you've returned. While I am disappointed.. This is to be expected.",textspeed)
        time.sleep(.5)
        typewrite_text(f"\nStill I do not regret choosing you, {name}. I can see that you are resilient.",textspeed)
        time.sleep(.5)
        clear_terminal()
        typewrite_text(f"\n..The {YELLOW}MOON{RESET} remains in the hands of the bastard. You must restore it."
                       f"\nYou will be reborn and I will lend you my strength once more.",textspeed)
        clear_terminal()
        typewrite_text(f"But know this: The path will grow darker.\nEventually, I will not be here to catch you.",textspeed)
        time.sleep(.5)
        typewrite_text(f"\nFor now your destiny awaits. The {YELLOW}MOON{RESET} calls you, {name}.\nI wish you good luck.",textspeed)
        time.sleep(1)
        playervals.specials.append("Charge")
        typewrite_text("\n(You learned CHARGE)",textspeed)
        time.sleep(1)

    elif playervals.deathcount == 2:
        typewrite_text("You are back again. ",textspeed)
        time.sleep(.5)
        typewrite_text("I must admit, this grows to be tiring.",textspeed)
        time.sleep(.5)
        typewrite_text(f"\nDo you not understand that the more you stumble, the farther our {YELLOW}MOON{RESET} drifts from us?"
                       f"\n{name}, you must be our hero. I have chosen you for a reason. Please do not mock my judgement.",textspeed)
        clear_terminal()
        typewrite_text("\n..Take my blessing. Do not waste it, young one.",textspeed)
        time.sleep(.5)
        typewrite_text(f"\nThe {YELLOW}MOON{RESET} does not wait,\nand I grow impatient.",textspeed)
        playervals.specials.append("Cure")
        time.sleep(1)
        typewrite_text("\n(You learned CURE)",textspeed)
        time.sleep(1)

    elif playervals.deathcount == 3:
        typewrite_text("A mockery. This is what you have become.",textspeed)
        time.sleep(.5)
        typewrite_text("\nYou falter again, and again.",textspeed)
        time.sleep(.5)
        typewrite_text("\nEach death is a crack in our world that ruptures the peace of everyone."
                       "\nHow many times must I pull you from the depths of failure?",textspeed)
        clear_terminal()
        typewrite_text(f"The {YELLOW}MOON{RESET} cries out, {name}.",textspeed)
        time.sleep(.5)
        typewrite_text("\nIt knows not who you are. \nShould I agree?" 
                       f"\nNo. Not yet. You were chosen, and you \033[1mwill\033[0m rise.",textspeed)
        time.sleep(.5)
        clear_terminal()
        typewrite_text(f"...But this is your last mercy.\nI wish for the best of you, {name}.",textspeed)
        playervals.specials.append("Swap")
        time.sleep(1)
        typewrite_text("\n(You learned SWAP)",textspeed)
        time.sleep(1)

    elif playervals.deathcount == 4:
        typewrite_text(f"{name}. ...You were meant to save us.\nTo bring back our {YELLOW}MOON{RESET}.",textspeed)
        time.sleep(.5)
        typewrite_text("I believed in you, \n..But perhaps I was misguided.",textspeed)
        time.sleep(.5)
        typewrite_text("\nI will grant you another gift.",textspeed)
        clear_terminal()
        typewrite_text(f"Bring my {YELLOW}MOON{RESET}. Or do not return.",textspeed)
        playervals.specials.append("Guard Break")
        time.sleep(1)
        typewrite_text("\n(You learned GUARD BREAK)",textspeed)
        time.sleep(1)

    elif playervals.deathcount == 5:
        typewrite_text(f"{name}, how much longer must I endure your failure?",textspeed)
        time.sleep(.5)
        typewrite_text("\nYou are nearly unworthy. It's funny how even now scraps of hope cling to you.",textspeed)
        time.sleep(.5)
        typewrite_text(" My patience has run dry.",textspeed)
        clear_terminal()
        typewrite_text("Survive. Or vanish from my sight forever.",textspeed)
        playervals.specials.append("Bite")
        time.sleep(1)
        typewrite_text("\n(You learned BITE)",textspeed)
        time.sleep(1)

    elif playervals.deathcount == 6:
        typewrite_text("...",textspeed)
        time.sleep(.5)
        typewrite_text("\nWretched insect.",textspeed)
        time.sleep(.5)
        typewrite_text(" I am beyond through with you. Your persistence has become delusion.",textspeed)
        clear_terminal()
        typewrite_text(f"\nThis is your last chance. If you waste it..." 
                       f"\nWe will all vanish with you.\nDo not fail me again.",textspeed)
        playervals.specials.append("Gamble")
        time.sleep(1)
        typewrite_text("\n(You learned GAMBLE)",textspeed)
        time.sleep(1)

    elif playervals.deathcount >= 7:
        typewrite_text(f"You just keep coming back..\nBring it.\nBring our {YELLOW}MOON{RESET}.\n..I grow weary.",textspeed)

    playervals.deathcount += 1
    time.sleep(1)
    clear_terminal()
    time.sleep(1.5)