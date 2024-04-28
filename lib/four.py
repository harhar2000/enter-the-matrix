from common import *

def first_function():
    paragraphs = ["\n Let's try defining the function unlock_door(code)"]

    wrap_and_print_text(paragraphs)

    def matches_unlock_door_definition(input):
        pattern = r"def unlock_door\(code\):\s*return code == '(\d+)'"
        return re.match(input, pattern)

    prompt = "Try defining the function here:"
    validate_user_input(prompt, matches_unlock_door_definition, "Try again")


if __name__ == '__main__':
    first_function()