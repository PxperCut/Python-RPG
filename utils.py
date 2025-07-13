import sys
import time
import os
import keyboard
import threading
import random

textspeed = 0.01
name="default name"

class Player:
    def __init__(self,ATK,HP,MAXHP,SP,MAXSP,inflictions,SOUL,deathcount,specials):
        self.atk=ATK
        self.hp=HP
        self.MAXHP=MAXHP
        self.SP=SP
        self.MAXSP=MAXSP
        self.inflictions=inflictions
        self.SOUL=SOUL
        self.deathcount=deathcount
        self.specials=specials

playervals=Player(1, #atk
                  10,#hp
                  10,#maxhp
                  10,#sp
                  15,#maxsp
                  [],#inflictions
                  0, #SOUL
                  0, #deathcount
                  ["Pass","Bash"]#specials
                  )


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

def apply_status(inflictions, status_name, duration):
    for i, (name, dur) in enumerate(inflictions):
        if name == status_name:
            inflictions[i] = (name, duration) 
            return
    inflictions.append((status_name, duration))
    
def weighted_choice(choices, key="weight"):
    total = sum(c[key] for c in choices)
    r = random.uniform(0, total)
    upto = 0
    for c in choices:
        w = c[key]
        if upto + w >= r:
            return c
        upto += w
    return choices[-1]

def clamp(val, min_val, max_val):
    if val > max_val:
        val = max_val
    elif val < min_val:
        val = min_val
    return val

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_image_list(image_list):
    for row in image_list:
        print(row)
    print("")

def delay_char(char, delay):
    base_delay = 0 if keyboard.is_pressed('shift') else delay

    if not keyboard.is_pressed('shift'):
        if char in ".!?":
            time.sleep(base_delay + 1)
        elif char in ",;:":
            time.sleep(base_delay + .8)
        else:
            time.sleep(base_delay)
    else: time.sleep(base_delay/2)

def typewrite_text(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        delay_char(char, delay)

def typewrite_text_sliced(textlist,delay):
    for row in textlist:
        for char in row:
            sys.stdout.write(char)
            sys.stdout.flush()
            delay_char(char,delay)
        print("")

def typewrite_text_async(text, delay):
    def worker():
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            delay_char(char, delay)
    threading.Thread(target=worker, daemon=True).start()