from common import *

def second_function(custom_delay=0.02):
    paragraphs = [
        "\nLet's continue with another example and infuse this function with logic.",
        "```",
        "def hack_door(code):",
        "    if code == '110799':",
        "        return 'Door unlocked.'",
        "    else:",
        "        return 'Access denied.'",
        "```",
        "Note the indentation. Indented code means that it belongs within the code of the line above",
        "This code snippet is our digital key. The `if` statement checks if the input code matches '110799'. If it does, the Matrix acknowledges our success and the door will unlock. If not, access is denied.",
        "To use this function, you call it with a potential passcode:",
        "```",
        "result = hack_door('110799')",
        "print(result)  # This prints: Door unlocked.",
        "result = hack_door('1999')",
        "print(result)  # This prints: Access denied.",
        "```",
        ""]

    wrap_and_print_text(paragraphs, width=width, delay=custom_delay)


# def link_three(name, custom_delay=0.02):
    paragraphs = [
        f"\n{name}, if one of our team needed you to unlock a door for them in The Matrix, you would type 'def unlock_door(code):', try it!"
    ]
    wrap_and_print_text(paragraphs, width=width, delay=custom_delay)

    def validate_input(prompt, validate_function, error_message, success_message, custom_delay=0.02):
        while True:
            user_input = input(prompt).strip()  # Capture input and strip() to remove extra whitespace

            if validate_function(user_input):
                print_slowly(success_message, delay=custom_delay)
                break
            else:
                print_slowly(error_message, delay=custom_delay)

    def matches_unlock_door_function(input):
        return input == "def unlock_door(code):"

    prompt = "Type here: \n\n"
    error_message = "\n\nA small mistake. Remember, to define this function, type 'def unlock_door(code):'"
    success_message = "\n\nExcellent! You're one step closer to becoming a proficient operator."

    validate_input(prompt, matches_unlock_door_function, error_message, success_message)



if __name__ == "__main__":
    width = get_terminal_width() 
    name = get_name_from_file()
    second_function()