import sys
import os
import time
from utils import clear_terminal, typewrite_text, print_image_list, textspeed,name
import cutie

import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

RESET = "\033[0m"
YELLOW = "\033[33m"

gradient_lines = [
    "\033[38;2;255;255;255m",
    "\033[38;2;255;255;229m",
    "\033[38;2;255;255;204m",
    "\033[38;2;255;255;153m",
    "\033[38;2;255;255;102m",
    "\033[38;2;255;255;51m",
    "\033[38;2;255;255;0m"
]


def intro_textfunc():
    while True:
        clear_terminal()
        lines = [
            "::::    ::::   ::::::::   ::::::::  ::::    ::: :::::::::   ::::::::  :::    ::: ::::    ::: :::::::::",
            "+:+:+: :+:+:+ :+:    :+: :+:    :+: :+:+:   :+: :+:    :+: :+:    :+: :+:    :+: :+:+:   :+: :+:    :+:",
            "+:+ +:+:+ +:+ +:+    +:+ +:+    +:+ :+:+:+  +:+ +:+    +:+ +:+    +:+ +:+    +:+ :+:+:+  +:+ +:+    +:+",
            "+#+  +:+  +#+ +#+    +:+ +#+    +:+ +#+ +:+ +#+ +#++:++#+  +#+    +:+ +#+    +:+ +#+ +:+ +#+ +#+    +:+",
            "+#+       +#+ +#+    +#+ +#+    +#+ +#+  +#+#+# +#+    +#+ +#+    +#+ +#+    +#+ +#+  +#+#+# +#+    +#+",
            "#+#       #+# #+#    #+# #+#    #+# #+#   #+#+# #+#    #+# #+#    #+# #+#    #+# #+#   #+#+# #+#    #+#",
            "###       ###  ########   ########  ###    #### #########   ########   ########  ###    #### #########"
        ]

        for color, line in zip(gradient_lines, lines):
            print(f"{color}{line}{RESET}")


        option = cutie.select(
            ["Start", "Info", "Exit"],
            selected_index=0,
            selected_prefix="\033[33;1m[*] \033[0m"
        )

        if option == 0:
            break

        elif option == 1:  # Info
            clear_terminal()
            print("\nMoonbound is a text based roguelike. At the moment, it is largely unfinished due to time constraints and there is no genuine way to beat the game... yet!" \
            "\nWith that said, here are the basic mechanics of the game.")
            print()
            print("Consider every run an experiment. The game is randomly generated, meaning each room is unique to your own run." \
            "\n"
            "\n* Use your map to locate the STAIRWELL, leading to the next floor." \
            "\n* Use SP (Skill points) to perform special moves."
            "\n* Look around! Some rooms contain a special surprise or character." \
            "\n* This game is MEANT TO BE DIFFICULT! \033[1mYOU WILL DIE A LOT.\033[0m")
            sub_option = cutie.select(["Back"], selected_index=0, selected_prefix="\033[33;1m[*] \033[0m")
            if sub_option == 0:
                continue  # back to main menu

        else:  # Exit
            clear_terminal()
            typewrite_text("Buh Bye!",textspeed)
            time.sleep
            sys.exit() 


    while True:
        clear_terminal()
        typewrite_text("Choose a name for yourself: ", textspeed)
        name = input("")
        typewrite_text(f"\nYou've chosen the name: '{YELLOW}{name}{RESET}'.", textspeed)
        time.sleep(0.5)
        typewrite_text("\nIs this your preferred name?\n", textspeed)
        choice = cutie.select(
            ["Yes, I'm happy with it.", "No, I want to change it."],
            ["happy with it", "not happy with it."],
            selected_index=0,
            selected_prefix="\033[33;1m[*] \033[0m"
        )

        if choice == 0:
            break
        elif choice == 1:
            pass

    typewrite_text("\nWonderful.\nNow, let me tell you a story.", textspeed)
    time.sleep(1)
    clear_terminal()
    time.sleep(1)
    typewrite_text(
        "Before nature flourished,\n"
        "When the world was empty and barren,\n"
        "There lived a single ruler—an idiot god consumed by his own greed.\n"
        "He hoarded the skies, the stars, and all things that were.\n"
        "And with that, he believed himself to be contempt.\n"
        "Until, of course,\n"
        "He heard whispers of something he did not have to his name.\n"
        "The " + YELLOW + "MOON" + RESET + " could certainly complete his hoard.\n"
        "His curiosity twisted to hunger.\n",
        textspeed
    )
    time.sleep(1)

    clear_terminal()
    time.sleep(1)
    typewrite_text(
        "In his obsession, he searched far and wide.\n"
        "He tore open the throats of galaxies to peer inside.\n"
        "He peeled the skin of stars without hesitation.\n"
        "But still, No " + YELLOW + "MOON" + RESET + ".\n"
        "And when he grew weary of his search,\n"
        "There, he saw it.\n"
        "Swollen with elation, he snatched the " + YELLOW + "MOON" + RESET + ", and at once, it was finally his.\n",
        textspeed
    )
    time.sleep(1)

    clear_terminal()
    time.sleep(1)
    typewrite_text(
        "Opening his fist, he saw now that he had been too careless. He had shattered the " + YELLOW + "MOON" + RESET + ".\n"
        "The god fell into a great sadness, his work now unmade.\n"
        "Yet he did not bother to see the folly that his grand plan had set in motion. With no " + YELLOW + "MOON" + RESET + ", the sky was cast with an eternal night.\n",
        textspeed
    )
    time.sleep(1)
    clear_terminal()
    typewrite_text(
        "Overcome with despair, the god sunk into the soil of the earth and created his tomb where he could wallow forevermore.\n"
        "In the darkness something evil was born. Monsters began to take shape.\n"
        "They began to slither into cracks of the world, but most of all, they gathered where their father had fallen.\n"
        "And so, there could be no peace.\n",
        textspeed
    )
    time.sleep(1)
    clear_terminal()
    typewrite_text(
        "I now call upon you to stand at the edge of his dungeon. You must confront the one who stole our dawn and plead with him to restore it.\n"
        "By any means necessary.\n"
        "Please, " + YELLOW + name + RESET + ", step carefully... and bring back our " + YELLOW + "MOON" + RESET + ".",
        textspeed
    )
