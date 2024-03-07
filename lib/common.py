import time                 # Delay between printing each character
import textwrap             # Wrap text to fit terminal
import os                   # Functionalities for interacting with OS. e.g. finding out terminal size
import sys                  # Interacting with interpreter. e.g. stdin checks to detect immediate user action
import select               # Script detects for keyboard input without halting execution.
import re                   # Regular Expression for try again or well done options 

def print_slowly(text, delay=0.075):           # Prints text slowly, character by character
    enter_pressed = False
    for char in text:
        if not enter_pressed:
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:   # Check for Enter key input
                sys.stdin.readline()
                delay = 0.001                           # Reduce delay 
                enter_pressed = True
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def wrap_and_print_text(paragraphs, width=70, delay=0.075):
    wrapped_text = '\n\n'.join([textwrap.fill(paragraph, width=width) for paragraph in paragraphs])
    print_slowly(wrapped_text, delay=delay)

def get_terminal_width(default=70):
    try:
        columns, _ = os.get_terminal_size()
        return columns
    except OSError:                                 # Default size if cannot determine
        return default

def get_name_from_file(file_path="namefile.txt"):
    try:
        with open(file_path, "r") as file:
            name = file.read().strip()
        return name
    except FileNotFoundError:
        print("File not found. Ensure the file path is correct.")  # REWRITE as user won't have access to filepath
        return None