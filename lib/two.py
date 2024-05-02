from common import *

def comments(custom_delay=0.02):
    paragraphs = [
        "",
        f"Ready {name}?", 
        "Leaving notes or comments for your team is crucial. These comments, marked by the '#' character cannot be deciphered by machines. # are messages for human eyes only, to explain functions without impacting execution",
        "# This is a comment. Nothing past the # will run. Use # to explain the code",
        "Show me you understand. Add a comment to explain the following line of code."
        ]
    
    wrap_and_print_text(paragraphs, width=width, delay=custom_delay)

    validate_user_input(
        prompt="\n total = x + y ",
        validation_function=lambda user_input: user_input.startswith("#"),
        error_message="\n\nRemember, you're just adding a # followed by an explanation of what the line of code does",
        custom_delay=custom_delay
    )
    print_slowly("\n\nWell done, you created your first comment", delay=custom_delay)


def first_function(custom_delay=0.02):
    width = get_terminal_width()
    paragraphs = [
        "",
        "Onto something more tangible:",
        "Functions are mini-programs, reusable blocks of code that perform specific tasks. A tool crafted once and used as needed",
        "Here's a simple function:",
        "```",
        "def add_one(num):",
        "    return num + 1",
        "```",
        "Let's break it down:",
        "** Name **: Every function has a name, e.g. add_one():. It's how we identify and call the function to do its job.",
        "** Parameter **: Functions often require inputs to work with. num is our function's parameter, the data needed to perform its task.",
        "Our add_one() function takes an input (num) and adds one to it. It's a clear demonstration of how functions accept an input, process it and return an output.",
        "To unleash a function, call it by its name and provide its required input, like so:",
        "```",
        "add_one(4)     # Calls the function with 4 as the input",
        "```",
        "Here, 4 is passed into add_one. The function adds one, returning 5.\n\n\n",
        "",
    ]
    wrap_and_print_text(paragraphs, width=width, delay=custom_delay) 
    # change prompt below to account for 0-9 potential number
    prompt = "We can mix functions together. To put the add_one() in action put a number of your choice within add_one() and place it within the 'print()' functions brackets. Remember to keep the number of brackets equal. For every opening bracket there needs to be a closing bracket!\n"
    wrapped_prompt = textwrap.fill(prompt, width=width)
    print_slowly(wrapped_prompt, delay=custom_delay)


    test = r"\s*print\s*\(\s*add_one\s*\(\s*([1-9][0-9]*)\s*\)\s*\)\s*"
    
    user_input = validate_user_input(
        prompt="", 
        validation_function=lambda user_input: re.fullmatch(test, user_input) is not None,
        error_message=f"\n\nDon't worry! Take 'add_one()', put your number within it's brackets and put all of that within the brackets of the print() function. You should have a total of 4 brackets\n",
        custom_delay=custom_delay
    ) 
    match = re.fullmatch(test, user_input).groups()[0]
    total = int(match)
    match = total + 1 
    
    
    print_slowly(f"\n\n{match}\n\nExcellent work! {user_input} takes the number {total}, adds 1 and because of the print() function, prints {match}\n", delay=custom_delay)


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