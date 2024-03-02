import sys
import os
import select
import time


def print_slowly(text, delay=0.075):  # Prints text slowly, character by character
    for char in text:
        if (
            sys.stdin in select.select([sys.stdin], [], [], 0)[0]
        ):  # Check for Enter key input
            line = sys.stdin.readline()
            delay = 0.001  # Reduce delay
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def get_terminal_width(default=70):
    try:
        columns, _ = os.get_terminal_size()
        return columns
    except OSError:  # Default size if cannot determine
        return default


def get_name_from_file():
    os.chdir("lib")
    with open("namefile.txt", "r") as file:
        name = file.read().strip()
    return name
