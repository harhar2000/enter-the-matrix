from main import get_terminal_width
import time                 # Delay between printing each character
import textwrap             # Wrap text to fit terminal
import os                   # Functionalities for interacting with OS. e.g. finding out terminal size
import sys                  # Interacting with interpreter. e.g. stdin checks to detect immediate user action
import select               # Script detects for keyboard input without halting execution.

def print_slowly(text, delay=0.075):           # Prints text slowly, character by character
    for char in text:
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:   # Check for Enter key input
            line = sys.stdin.readline()
            delay = 0.001                           # Reduce delay 
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_terminal_width(default=70):
    try:
        columns, _ = os.get_terminal_size()
        return columns
    except OSError:                                 # Default size if cannot determine
        return default

def get_name_from_file():
    with open("namefile.txt", "r") as file:
        name = file.read().strip()
    return name

## FILE BEGIN

def link_two(name, custom_delay=0.02):
    width = get_terminal_width()
    paragraphs = [
        f"{name}, Create a function that removes the first and last characters of a string. Use one parameter - the original string. Don't worry about strings with less than two characters\n",
        " "
    ]

    wrapped_text = '\n\n'.join([textwrap.fill(paragraph, width=width) for paragraph in paragraphs])  # Wrap each paragraph to fit terminal and join with double newlines

    print_slowly(wrapped_text, delay=custom_delay)

def reduce_string(string):
    return string[1:len(string)-1]

print(reduce_string("hellooo")) # DECIDE VARIABLE

if __name__ == "__main__":
    name = get_name_from_file()
    link_two(name)