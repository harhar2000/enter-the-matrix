from common import *

def comments(custom_delay=0.02):
    paragraphs = [
        "",
        f"Ready {name}?", 
        "Leaving notes or comments for your team is crucial. These comments, marked by the '#' character cannot be deciphered by machines. # are messages for human eyes only, to explain function without impacting execution",
        "# This is a comment. Nothing past the # will run. Use # to explain the code",
        "Show me you understand. Add a comment to explain the following line of code."
        ]
    
    wrap_and_print_text(paragraphs, width=width, delay=custom_delay)


    while True:
        user_input = input("\n total = x + y ").lstrip()  #  Capture input and strip() to remove extra whitespace

        if not user_input.startswith("#"):
            print_slowly("\n\nRemember, you're just adding a # followed by an explanation of what the line of code does", delay=custom_delay)    ### Reword this with AI to be different each time it prints?
        else:
            print_slowly("\n\nWell done, you created your first comment", delay=custom_delay)
            break


def first_function(custom_delay=0.02):
    paragraphs = [
        "",
        "Onto something more tangible: Function are mini-programs, reusable blocks of code that perform specific tasks. A tool crafted once and used as needed",
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

    wrap_and_print_text(paragraphs, width=width, delay=custom_delay) 

    while True:
        user_input = input().lstrip()  #  Capture input and strip() to remove extra whitespace

        if not re.fullmatch("print\(add_one\(\W*4\W*\)\)", user_input): # Look for other ways to simplify this logic <-, wrap that code into a function and pass paramter into it, call that function when needed
            print_slowly("\n\nDon't worry! Take add_one(4) and put it as it is within the brackets of the print() function. You should have a total of 4 brackets", delay=custom_delay)    ### Reword this with AI infite times?
        else:
            print("\n5") # Actually print 5 as a result of input rather than printing 5 because it says to in code
            print_slowly("\n\nExcellent work! add_one() taes the number 4, adds 1 and because of the print() function, prints 5\n", delay=custom_delay)
            break


def two_final_section(custom_delay=0.02) :
    paragraphs =[
        "print() displays our functions result when called, proving even simple functions can be powerful tools in the right hands.",
        f"Remember {name}, in the Matrix, knowledge is power. These basics allow you to start manipulating the code around you, bending the Matrix to our will. Keep practicing and soon you'll be writing code that can unlock doors, bending physics and more. This is just the beginning.",
        "\n\n Enter 'python three.py' into your terminal to continue"
    ]

    wrap_and_print_text(paragraphs, width=width, delay=custom_delay)


if __name__ == "__main__":
    width = get_terminal_width() 
    name = get_name_from_file()
    comments()
    first_function()
    two_final_section()