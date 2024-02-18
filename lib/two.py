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
    paragraphs = [
        "In the vast, complex world of the Matrix, leaving notes for your fellow rebels is crucial. These notes, or comments, are marked by the # character. They're like whispers in the code, meant for human eyes only. The Machines can't read them. They're our way of leaving messages, explaining what a piece of code does, without affecting its execution.",
        "# This is a comment. Python doesn't run this line.",
        "# Use comments to explain what your code does, making it easier for others (and yourself) to understand later.",
        "Now, onto something more tangible: functions. A function is a mini-program, a reusable block of code designed to perform a specific task. Think of it as a tool you craft once and then use as needed, modifying the Matrix with precision.",
        "Here's a simple function:",
        "```",
        "def add_one(num):",
        "num = num + 1"
        "  return num",
        "```",
        "Let's break it down:",
        "Name: Every function has a name, in this case, add_one. It's how we identify and call upon the function to do its job.",
        "Parameter: Functions often require input to work with. num is our function's parameter, the piece of data it needs to perform its task.",
        "Body: The body of the function, processes the input and returns an output. In Python, indentation marks the body, setting it apart from the rest.",
        "Our add_one function takes an input (num) and simply adds one to it. It's a clear demonstration of how functions accept input, process it and return an output.",
        "To unleash a function's power, you call it by its name and provide any required input, like so:",
        "```",
        "result = add_one(4)  # Calls the function with 4 as the input",
        "```\n",
        "Here, 4 is passed to add_one, taking the place of num inside the function. The function then adds one and returns 5, completing its task.",
        "Want to see the function in action? Let's use print to make its work visible:",
        "```",
        "print(\"add_one(4)) # returns: 5",
        "```",
        "This line will display the result of our function when called with 4 as the argument, proving that even the simplest functions can be powerful tools in the right hands.",
        "Remember, in the Matrix, knowledge is power. These basics allow you to start manipulating the code around you, bending the Matrix to our will. Keep practicing, and soon you'll be writing code that can unlock doors, bending physics and much more. This is just the beginning."
    ]

    wrapped_text = '\n\n'.join([textwrap.fill(paragraph, width=width) for paragraph in paragraphs])  # Format text to fit the terminal width
    print_slowly(wrapped_text, delay=custom_delay)

if __name__ == "__main__":
    name = get_name_from_file()
    link_two()