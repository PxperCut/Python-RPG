import sys,time
import cutie
import utils
from utils import clear_terminal, typewrite_text, textspeed,playervals
import dictionary
from dictionary import useitem,inspectitem

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

inv = []
maxinvsize = 8

def clearinventory():
    inv.clear()

def storeitem(item):
    if not len(inv)>maxinvsize:
        inv.append(item)

def removeitem(item):
    inv.remove(item)

def openinv():
    while True:
        clear_terminal()
        options = []
        print("\033[1m---Inventory---\033[0m")
        print()
        print(f"\033[1mSOUL:\033[0m{playervals.SOUL}")
        print(f"\033[1mHP:\033[0m{playervals.hp}")
        print(f"\033[1mSP:\033[0m{playervals.SP}")
        print(f"\033[1mDEATHS:\033[0m{playervals.deathcount}")
        print()
        print(f"{len(inv)}/{str(maxinvsize)}")
        for item in inv:
            options.append(item)
        options.append("!space")
        options.append("Back")

        selection = cutie.select(options, selected_index=len(options)-1, selected_prefix="\033[33;1m[*] \033[0m")
        
        if options[selection] == "Back":
            break

        else:
            selecteditem = options[selection]
            while True:
                clear_terminal()
                print(f"-{selecteditem}")
                suboptions = ["Use", "Inspect", "Discard", "!space", "Back"]#give options
                subselection = cutie.select(suboptions, selected_prefix="\033[33;1m[*] \033[0m")
        
                if suboptions[subselection] == "Back":
                    return
                else:
                    clear_terminal()    
                    if suboptions[subselection]=="Inspect":#inspections
                        print(inspectitem(selecteditem))#find inspection from dictionary based on item
                        cutie.select(["Back"],selected_prefix="\033[33;1m[*] \033[0m")
                    elif suboptions[subselection]=="Use":#use
                        text,hpdif,spdif,Extra=useitem(selecteditem)#find use from dictionary based on item
                        typewrite_text(text,textspeed)
                        time.sleep(.5)

                        if not Extra==None: #any extra attributes from an item...
                            if Extra=="Decay":
                                typewrite_text("\nI was inflicted with Decay!",textspeed)
                        if not Extra==None: #any extra attributes from an item...
                            if Extra=="Cure Ailments":
                                typewrite_text("\nI was cured of any ailments.",textspeed)
                        if hpdif!=0:#if hp increased tell the player
                            if playervals.hp==playervals.MAXHP:
                                typewrite_text("\n\033[1mMy HP was maxxed out!\033[0m", textspeed)
                            else:
                                if hpdif>0:
                                    typewrite_text(f"\n\033[1m(I recovered {hpdif} HP)\033[0m", textspeed)
                                else:
                                    typewrite_text(f"\n\033[1m(I lost {hpdif} HP)\033[0m", textspeed)

                        if spdif!=0:#if sp increased tell the player
                            if playervals.SP==playervals.MAXSP:
                                typewrite_text("\n\033[1mMy SP was maxxed out!\033[0m", textspeed)
                            else:
                                if spdif>0:
                                    typewrite_text(f"\n\033[1m(I recovered {spdif} SP)\033[0m", textspeed)
                                else:
                                    typewrite_text(f"\n\033[1m(I lost {spdif} SP)\033[0m", textspeed)
                        removeitem(selecteditem)
                        time.sleep(1)
                        return selecteditem
                    elif suboptions[subselection]=="Discard":
                        inv.remove(item)
                        typewrite_text(f"The {str(item)} was thrown away.",textspeed)
                        time.sleep(1)
    return

playervals.SOUL=10