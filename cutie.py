"""
Commandline User Tools for Input Easification + Dynamic Descriptions
"""

__version__ = "0.3.2"
__author__ = "Hans / Kamik423, modified by Keegan"
__license__ = "MIT"

import getpass
from typing import List, Optional

import readchar
from colorama import init

init()

class DefaultKeys:
    interrupt: List[str] = [readchar.key.CTRL_C, readchar.key.CTRL_D]
    select: List[str] = [readchar.key.SPACE]
    confirm: List[str] = [readchar.key.ENTER]
    delete: List[str] = [readchar.key.BACKSPACE]
    down: List[str] = [readchar.key.DOWN, "j"]
    up: List[str] = [readchar.key.UP, "k"]


def get_number(
    prompt: str,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    allow_float: bool = True,
) -> float:
    return_value: Optional[float] = None
    while return_value is None:
        input_value = input(prompt + " ")
        try:
            return_value = float(input_value)
        except ValueError:
            print("Not a valid number.\033[K\033[1A\r\033[K", end="")
        if not allow_float and return_value is not None:
            if return_value != int(return_value):
                print("Has to be an integer.\033[K\033[1A\r\033[K", end="")
                return_value = None
        if min_value is not None and return_value is not None:
            if return_value < min_value:
                print(f"Has to be at least {min_value}.\033[K\033[1A\r\033[K", end="")
                return_value = None
        if max_value is not None and return_value is not None:
            if return_value > max_value:
                print(f"Has to be at most {max_value}.\033[1A\r\033[K", end="")
                return_value = None
        if return_value is not None:
            break
    print("\033[K", end="")
    if allow_float:
        return return_value
    return int(return_value)


def secure_input(prompt: str) -> str:
    return getpass.getpass(prompt + " ")

from termcolor import colored

def select(
    options: List[str],
    caption_indices: Optional[List[int]] = None,
    deselected_prefix: str = "\033[1m[ ]\033[0m ",
    selected_prefix: str = "\033[1m[\033[32;1mx\033[0;1m]\033[0m ",
    caption_prefix: str = "",
    selected_index: int = 0,
    confirm_on_select: bool = True,
    descriptions: Optional[dict] = None,
) -> int:
    """Interactive menu with optional dynamic inline descriptions."""
    
    if caption_indices is None:
        caption_indices = []

    visible_lines = 0
    for opt in options:
        visible_lines += 1

    print("\n" * visible_lines)

    while True:
        print(f"\033[{visible_lines}A", end="")
        for i, option in enumerate(options):
            print("\033[K", end="") 

            if option == "!space":
                print("")
            elif option == "!desc":
                desc = descriptions.get(options[selected_index], "") if descriptions else ""
                if desc:
                    print(f"\033[1m\033[90m#{desc}\033[0m")
                else:
                    print("")
            elif i in caption_indices:
                print(f"{caption_prefix}{option}")
            else:
                prefix = selected_prefix if i == selected_index else deselected_prefix
                print(f"{prefix}{option}")

        keypress = readchar.readkey()

        if keypress in DefaultKeys.up:
            new_index = selected_index
            while new_index > 0:
                new_index -= 1
                if new_index not in caption_indices and options[new_index] not in ("!space", "!desc"):
                    selected_index = new_index
                    break

        elif keypress in DefaultKeys.down:
            new_index = selected_index
            while new_index < len(options) - 1:
                new_index += 1
                if new_index not in caption_indices and options[new_index] not in ("!space", "!desc"):
                    selected_index = new_index
                    break

        elif (
            keypress in DefaultKeys.confirm
            or (confirm_on_select and keypress in DefaultKeys.select)
        ):
            break

        elif keypress in DefaultKeys.interrupt:
            raise KeyboardInterrupt

    return selected_index
