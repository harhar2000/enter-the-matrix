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
        "",
        f"Ready {name}?", 
        "Leaving notes or comments for your fellow rebels is crucial. These comments, marked by the '#' character cannot be deciphered by the machines. # are messages for human eyes only, to explain function without impacting execution",
        "# This is a comment. Nothing past the # will run. Use # to explain the code",
        "Show me you understand. Add a comment to the following line of code."
        ]
    
    wrapped_text = '\n\n'.join([textwrap.fill(paragraph, width=width) for paragraph in paragraphs])  # Wrap each paragraph to fit terminal and join with double newlines
    print_slowly(wrapped_text, delay=custom_delay)

    while True:
        user_input = input("\n total = x + y ").lstrip()  #  Capture input and strip() to remove extra whitespace

        if not user_input.startswith("#"):
            print_slowly("\n\nRemember, you're just adding a # followed by an explanation of what the line of code does", delay=custom_delay)    ### Reword this with AI infite times?
        else:
            print_slowly("\n\nWell done, you created your first comment", delay=custom_delay)
            break



def next_section(custom_delay=0.02):
    width = get_terminal_width()
    paragraphs = [
        "",
        "Now onto something more tangible: Function are mini-programs, reusable blocks of code that perform specific tasks. A tool crafted once and used as needed",
        "Here's a simple function:",
        "",
        "```",
        "def add_one(num):",
        "    return num + 1",
        "```",
        "",
        "Let's break it down:",
        "Name: Every function has a name, e.g. add_one():. It's how we identify and call the function to do its job.",
        "Parameter: Functions often require inputs to work with. num is our function's parameter, the data needed to perform its task.",
        "Our add_one() function takes an input (num) and adds one to it. It's a clear demonstration of how functions accept an input, process it and return an output.",
        "To unleash a function, call it by its name and provide its required input, like so:",
        "",
        "```",
        "add_one(4)     # Calls the function with 4 as the input",
        "```",
        "",
        "Here, 4 is passed to add_one. The function adds one, returning 5.",
        "We can mix functions together. To put the function in action and see 'add_one(4)' printed in your terminal, put it within the 'print()' functions brackets. ",
        "Remember to keep the number of brackets equal. For every opening bracket there needs to be a closing bracket!"
    ]

    wrapped_text = '\n\n'.join([textwrap.fill(paragraph, width=width) for paragraph in paragraphs])  # Wrap each paragraph to fit terminal and join with double newlines
    print_slowly(wrapped_text, delay=custom_delay)

    while True:
        user_input = input().lstrip()  #  Capture input and strip() to remove extra whitespace

        if not user_input.startswith("print(add_one(4))"):
            print_slowly("\n\nDon't worry! Take add_one(4) and put it as it is within the brackets of the print() function. You should have a total of 4 brackets", delay=custom_delay)    ### Reword this with AI infite times?
        else:
            print("\n5")
            print_slowly("\n\nExcellent work! add_one() takes the number 4, adds 1 and because of the print() function, prints 5\n", delay=custom_delay)
            break


def two_final_section(custom_delay=0.02):
    width = get_terminal_width()
    paragraphs =[
        "print() displays our functions result when called, proving even simple functions can be powerful tools in the right hands.",
        f"Remember {name}, in the Matrix, knowledge is power. These basics allow you to start manipulating the code around you, bending the Matrix to our will. Keep practicing and soon you'll be writing code that can unlock doors, bending physics and more. This is just the beginning.",
        "\n\n Enter 'python three.py' into your terminal to continue"
    ]

    wrapped_text = '\n\n'.join([textwrap.fill(paragraph, width=width) for paragraph in paragraphs])  # Format text to fit the terminal width

    print_slowly(wrapped_text, delay=custom_delay)


if __name__ == "__main__":
    name = get_name_from_file()
    link_two()
    next_section()
    two_final_section()