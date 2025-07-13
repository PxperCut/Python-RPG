import sys
import os
import time
import random
import cutie
from termcolor import colored
import copy 

#utils
import utils
from utils import clear_terminal, typewrite_text, print_image_list, name, weighted_choice,playervals

import introduction
from introduction import intro_textfunc

import Inventory
from Inventory import openinv,storeitem,inv,maxinvsize,clearinventory


import battle
from battle import Battle

import dictionary
from dictionary import sayitemroom,saymonsterroom,entityroom,interactwentity,deathmessage

textspeed = 0.04

test_image_list = [
    "___ ____ ____ ___",
    " |  |___ [__   | ",
    " |  |___ ___]  | "
]

# ---------------------- map gen -------------------------

def generate_map(rows=5, cols=5, max_path_length=14):
    while True:
        grid = [[2 for _ in range(cols)] for _ in range(rows)]  # 2 = wall
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        start_col = random.randint(0, cols - 1)
        start_pos = (0, start_col)
        player_position = [0, start_col]

        path_stack = [start_pos]
        visited[0][start_col] = True
        grid[0][start_col] = 1  # 1 = path
        path_cells = [start_pos]
        path_count = 1
        reached_bottom = False

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while path_stack:
            row, col = path_stack[-1]
            if path_count >= max_path_length:
                break

            random.shuffle(directions)
            moved = False

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    grid[new_row][new_col] = 1
                    path_stack.append((new_row, new_col))
                    path_cells.append((new_row, new_col))
                    path_count += 1
                    moved = True
                    if new_row == rows - 1:
                        reached_bottom = True
                    break

            if not moved:
                path_stack.pop()

        if reached_bottom:
            break
    edge_path_tiles = [
        (r, c) for r in range(rows) for c in range(cols)
        if grid[r][c] == 1 and (r in [0, rows - 1] or c in [0, cols - 1])
    ]

    valid_rooms = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]

    return grid, player_position, valid_rooms

def print_map(grid, player_position):
    for row in range(len(grid)):
        line = ""
        for col in range(len(grid[0])):
            if (row, col) == tuple(player_position):
                line += "p "

            elif grid[row][col] == 2:
                line += "# "
            elif grid[row][col] == 1:
                line += ". "
            elif grid[row][col] == 3:
                line += "E "
        print(line)
    print()

def print_map_discovered(grid, player_position, discoveries):
    for row in range(len(grid)):
        line = ""
        for col in range(len(grid[0])):
            if (row, col) == tuple(player_position):
                line += "p "
                continue

            if grid[row][col] == 2:
                line += "# "

            if [row, col] not in discoveries and grid[row][col] != 2:
                line += "? "
            elif grid[row][col] == 1:
                line += ". "

            elif grid[row][col] == 3:
                line += "E " 


        print(line)
    print()

# ---------------------- inventory ----------------------

def clear_lines(n): 
    for _ in range(n):
        print("\033[F\033[K", end='') #\033[F moves cursor up one line, \033[K clears that line :)
# ---------------------- room calculation ----------------------

#if the room is an item room, we can assign the available items
#if the room is an enemy room, we can store a variable to see if any monsters are left in that room.

Room_types = {
    "ITEM ROOM": {
        "weight": 5,
        "subtypes": [
            {
                "subtype": "Sporeshroom-Room",
                "weight": 4, #weights act as rarity, a heigher weight means more likely
                "items": [{"name": "Sporeshroom"}]
            },
            {
                "subtype": "Sporecap-Room",
                "weight": 5,
                "items": [{"name": "Sporecap"}]
            },
            {
                "subtype": "Podium-Room",
                "weight": 3,
                "items": [{"name": "Lotus Flower"},
                          {"name": "SP Potion"}]
            },
            {
                "subtype": "Tree-Room",
                "weight": 5,
                "items": [{"name": "Blood Apple"}]
            },
            {
                "subtype": "Corpse-Room",
                "weight": 5,
                "items": [{"name": "Lichen Wrap"}]
            },
            {
                "subtype": "Corpse-Room",
                "weight": 5,
                "items": [{"name": "Lichen Wrap"}]
            },
            {
                "subtype": "Shrine-Room",
                "weight": 4,
                "items": [{"name": "Lotus Flower"}]
            },
            {
                "subtype": "Berry-Room",
                "weight": 4,
                "items": [{"name": "Nightshade Berry"}]
            },
            {
                "subtype": "Empty-Room",
                "weight": 3,
                "items": []
            },
            {
                "subtype": "Oil-Lamp-Room",
                "weight": 3,
                "items": [{"name": "Nightshade Oil"}]
            },
            {
                "subtype": "Fern-Room",
                "weight": 2,
                "items": [{"name": "Fern Leaf"}]
            }
        ]
    },

    "ENEMY ROOM": {
        "weight": 100,
        "subtypes": [
            {
                "subtype": "Gremlin Room",
                "weight": 5,
                "defeated": False
            },
            {
                "subtype": "Eyeball Room",
                "weight": 5,
                "defeated": False
            },
            {
                "subtype": "Slime Room",
                "weight": 5,
                "defeated": False
            },
            {
                "subtype": "Turtine Room",
                "weight": 5,
                "defeated": False
            },
            {
                "subtype": "Rotter Room",
                "weight": 5,
                "defeated": False
            },
            {
                "subtype": "Grub Room",
                "weight": 5,
                "defeated": False
            }
        ]
    },

    "ENTITY ROOM": {
        "weight": 5,
        "subtypes": [
            {
                "subtype": "Merchant",#room name
                "weight": 5,
                "chars": ["Merchant"]
            },
            {
                "subtype": "Knight",
                "weight": 4,
                "chars": ["Knight"]
            },
            {
                "subtype": "Hero",
                "weight": 19,
                "chars": ["Stranger"],
                "defeated":False
            },
        ]
    }
}



def calculate_room(grid, player_position, room_data):

    coord = (player_position[0], player_position[1])
    directions = {
        "North": (-1, 0),
        "South": (1, 0),
        "West": (0, -1),
        "East": (0, 1)
    }

    exits = []

    for direction, (dr, dc) in directions.items():
        r, c = player_position[0] + dr, player_position[1] + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] != 2:
                exits.append(direction)

    if coord in room_data:  #If room type is...
        #print(room_data[coord]) --this will print the current rooms data

        room_type = room_data[coord]["type"] #we can retrieve specifications for the relative data for this room, by accessing the key through it's coordinate on our map.
        room_subtype_data = room_data[coord]["subtype"] #same w/ its subtype's data
        items=None

        if room_type == "ITEM ROOM":

            items = room_subtype_data["items"]
            text=sayitemroom(room_subtype_data["subtype"],len(items))
            typewrite_text(text,textspeed)

        elif room_type == "ENEMY ROOM":
            result,text = saymonsterroom(room_subtype_data["subtype"], room_subtype_data["defeated"])
            if result == "defeated":
                room_subtype_data["defeated"] = result#if monster was killed
                typewrite_text(text,textspeed)
            else:#if player is dead
                deathmessage()
                return "dead"
        elif room_type == "ENTITY ROOM": #entity room
            defeated=False
            if "defeated" in room_subtype_data:
                defeated=room_subtype_data["defeated"]
            entityroom(room_subtype_data["subtype"],defeated)
    if grid[coord[0]][coord[1]] == 3:#exit is present
        typewrite_text("\nThere is a stairwell in this room.", textspeed)

    print("\n")
    if len(exits) == 1:
        description = f"There is only one way forward. A passage leads to the {exits[0].lower()}."
    elif len(exits) == 2:
        description = f"I can see exits to the {exits[0].lower()} and {exits[1].lower()}."
    else:
        last = exits[-1]
        others = exits[:-1]
        description = f"Looking around, I spot ways out to the {', '.join(e.lower() for e in others)}, and {last.lower()}."
    typewrite_text(description, textspeed)

    return items

# ---------------------- game handler --------------------------

    
def main():

    #intro_textfunc()  #uncomment me later
    #time.sleep(1)

    while True:

        #starting stats

        clearinventory()
        playervals.hp=playervals.MAXHP
        playervals.SP=playervals.MAXSP
        playervals.SOUL=0
        
        #starting inv

        storeitem("Lotus Flower")
        storeitem("Buttery Pie")
        
        while True:
            clear_terminal()
            typewrite_text("A tingle flows down my spine as I stare at the entrance to The Dungeon. Dry leaves litter the flooring from the forest behind me." \
            "\nThis is it." \
            "\nThere's no turning back now.",textspeed)
            print()
            menu_options=["Enter the dungeon.","Check Inventory"]
            choice = cutie.select(menu_options, selected_prefix="\033[33;1m[*] \033[0m",selected_index=0)
            choice_text = menu_options[choice].strip()
            if choice_text == "Check Inventory":
                clear_terminal()
                openinv()
            else:
                break
        
        exit_placed=False
        discoveries = [] #room coords to define each room
        room_data = {} #coords, room_type, etc...

        grid, player_position, valid_rooms = generate_map(5, 5, random.randint(7, 10))#gen map
        clear_terminal()
        
        while True:
            clear_terminal()
            
            #room determination
            if not [player_position[0],player_position[1]] in discoveries: #if room isnt already discovered,
                discoveries.append([player_position[0],player_position[1]]) #then we can discover this room

                room_type_choices = [{"name": k, "weight": v["weight"]} for k, v in Room_types.items()]
                selected_type_data = weighted_choice(room_type_choices)
                room_type = selected_type_data["name"]

                subtype_list = Room_types[room_type]["subtypes"]
                room_subtype = copy.deepcopy(weighted_choice(subtype_list))

                #we're using "copy" here bc i majorly messed up earlier and it was giving every room subtype the same data
                room_data [player_position[0],player_position[1]] = {"type": room_type, "subtype": room_subtype} #store the room's data so we remember its info

            #exit determination
            if not exit_placed and len(discoveries) == len(valid_rooms): #if there isn't already an exit, and we've already explored all rooms.
                grid[player_position[0]][player_position[1]] = 3 #that also we can make an exit on the same coordinate we're already on!
                exit_placed = True

            iteminfo = calculate_room(grid, player_position, room_data)
            
            if iteminfo=="dead":#if the player is dead...
                break#Restart the run!
            #item calc
            menu_options = []

            if "chars" in room_subtype:
                for entity in room_subtype["chars"]:
                    menu_options.append(entity)
                    menu_options.append("!space")

            if iteminfo:
                for item in iteminfo:
                    menu_options.append("Take "+item["name"].upper()) #for every obj in room, add that to our options.
                menu_options.append("!space")
                
            #only show movement option if valid
            if player_position[0] > 0 and grid[player_position[0] - 1][player_position[1]] != 2:
                menu_options.append("Move NORTH")
            if player_position[0] < len(grid) - 1 and grid[player_position[0] + 1][player_position[1]] != 2:
                menu_options.append("Move SOUTH")
            if player_position[1] > 0 and grid[player_position[0]][player_position[1] - 1] != 2:
                menu_options.append("Move WEST")
            if player_position[1] < len(grid[0]) - 1 and grid[player_position[0]][player_position[1] + 1] != 2:
                menu_options.append("Move EAST")
            if grid[player_position[0]][player_position[1]] == 3: #on exit tile
                menu_options.append("Take Exit")
            menu_options.append("!space")
            menu_options.append("Check Map")
            menu_options.append("Check Inventory")

            print("")
            choice = cutie.select(menu_options, selected_prefix="\033[33;1m[*] \033[0m",selected_index=0)
            choice_text = menu_options[choice].strip()
            
            delta_row, delta_col = 0, 0
            if choice_text == "Move NORTH":
                delta_row, delta_col = -1, 0
            elif choice_text == "Move SOUTH":
                delta_row, delta_col = 1, 0
            elif choice_text == "Move WEST":
                delta_row, delta_col = 0, -1
            elif choice_text == "Move EAST":
                delta_row, delta_col = 0, 1
            elif choice_text == "Check Map":
                clear_terminal()
                print_map_discovered(grid, player_position,discoveries)
                options = cutie.select(["Back"],selected_prefix="\033[33;1m[*] \033[0m",selected_index=0)
                if options==["Back"]:
                    continue

            coord = (player_position[0], player_position[1])
            
            if "chars" in room_data[coord]["subtype"]:
                for entity in room_data[coord]["subtype"]["chars"]:
                    if choice_text == entity:
                        if "defeated" in room_data:
                            dead = room_data["defeated"] = interactwentity(entity, room_data["defeated"])
                            room_data[coord]["subtype"]["chars"].clear() 

                            if dead == "dead":
                                deathmessage()
                                return "dead"
                        else:
                            interactwentity(entity, room_subtype)



            elif choice_text == "Check Inventory":
                clear_terminal()

                openinv()

            elif choice_text.startswith("Take "):
                item_name = choice_text[5:].capitalize()

                clear_terminal()
                    
                if not len(inv) == maxinvsize:
                    storeitem(item["name"])
                    
                    room_items = room_data[coord]["subtype"]["items"]
                    room_data[coord]["subtype"]["items"] = [
                        item for item in room_items if item["name"].lower() != item_name.lower()
                    ]
                    
                    typewrite_text(f"I picked up the {item_name}.", textspeed)
                else:
                    typewrite_text("My inventory is full.", textspeed)
                time.sleep(1)

            new_row = player_position[0] + delta_row
            new_col = player_position[1] + delta_col

            #movement
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] != 2:
                    player_position[0] = new_row
                    player_position[1] = new_col

#v dont delete me, this importantv
if __name__ == "__main__":
    main()

