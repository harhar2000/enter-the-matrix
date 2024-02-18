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


def link_two(custom_delay=0.02):
    width = get_terminal_width()
    paragraphs = ["\n\nLeaving notes for your fellow rebels is crucial. These notes or comments, are marked by the '#' character which the machines cannot decipher. Messages within the code for human eyes only, explaining its function without impacting execution",
        "# This is a comment. Nothing past the # will run. Use them to explain the code helping others and yourself understand later",
        "Onto something more tangible: Function are mini-programs, reusable blocks of code performing specific tasks. A tool crafted once and used as needed",
        "Here's a simple function:",
        "```",
        "def add_one(num):",
        "    return num + 1",
        "```",
        "Let's break it down:",
        "Name: Every function has a name, e.g. add_one(). It's how we identify and call the function to do its job.",
        "Parameter: Functions often require inputs to work with. num is our function's parameter, the piece of data it needs to perform its task.",
        "Body: The body processes the input and returns an output.",
        "Our add_one() function takes an input (num) and adds one to it. It's a clear demonstration of how functions accept input, process it and return an output.",
        "To unleash a function, you call it by its name and provide any required input, like so:",
        "```",
        "add_one(4)  # Calls the function with 4 as the input",
        "```",
        "Here, 4 is passed to add_one. The function adds one, returning 5.",
        "Want to see the function in action? Use print to make its work visible:",
        "```",
        "print(add_one(4))"
        "```",
        "print() displays our functions result when called, proving even simple functions can be powerful tools in the right hands.",
        "Remember, in the Matrix, knowledge is power. These basics allow you to start manipulating the code around you, bending the Matrix to our will. Keep practicing and soon you'll be writing code that can unlock doors, bending physics and more. This is just the beginning.",
        "\n\n Enter 'python three.py' into your terminal to continue"
    ]

    wrapped_text = '\n\n'.join([textwrap.fill(paragraph, width=width) for paragraph in paragraphs])  # Format text to fit the terminal width

    print_slowly(wrapped_text, delay=custom_delay)


if __name__ == "__main__":
    name = get_name_from_file()
    link_two()