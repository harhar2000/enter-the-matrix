import time                 # Delay between printing each character
import textwrap             # Wrap text to fit terminal
import os                   # Functionalities for interacting with OS. e.g. finding out terminal size
import sys                  # Interacting with interpreter. e.g. stdin checks to detect immediate user action
import select               # Script detects for keyboard input without halting execution.
import re                   # Regular Expression for try again or well done options 
import msvcrt

def print_slowly(text, delay=0.075):           # Prints text slowly, character by character
    enter_pressed = False
    for char in text:
        if not enter_pressed:
            # The next line is for mac, get a conditional for windows and mac that works for both
            if enter_pressed_for_platform():
                delay = 0.001                           # Reduce delay
                enter_pressed = True
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def enter_pressed_for_platform() -> bool:
    if sys.platform.startswith('win'):
        if msvcrt.kbhit():  # Check if a key has been pressed
            key = msvcrt.getch()  # Get the pressed key
            if key == b'\r':  # Check if the key is the Enter key
                return True

        return False

    else: # mac/UNIX
        enter_pressed = sys.stdin in select.select([sys.stdin], [], [], 0)[0]
        if enter_pressed:
             sys.stdin.readline() # unsure what this does, but looks like it's needed for Mac not windows

def wrap_and_print_text(paragraphs, width=70, delay=0.075):
    wrapped_text = '\n\n'.join([textwrap.fill(paragraph, width=width) for paragraph in paragraphs])
    print_slowly(wrapped_text, delay=delay)

def get_terminal_width(default=70):
    try:
        columns, _ = os.get_terminal_size()
        return columns
    except OSError:                                 # Default size if cannot determine
        return default

def get_name_from_file(operation="read", name=None, file_path="namefile.txt"):
    if operation == "write" and name:
        with open(file_path, "w") as file:
            file.write(name)
    elif operation == "read":
        try:
            with open(file_path, "r") as file:
                return file.read().strip()
        except FileNotFoundError:
            print("Name file not found.")
            return None

def validate_user_input(prompt, validation_function, error_message, custom_delay=0.02):
    while True:
        user_input = input(prompt).lstrip()  # Capture input and strip() to remove extra whitespace
        if validation_function(user_input):
            return user_input
        else:
            print_slowly(error_message, delay=custom_delay)
