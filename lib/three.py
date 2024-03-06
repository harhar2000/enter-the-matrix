from common import *

def link_ten(custom_delay=0.02):
    width = get_terminal_width()
    paragraphs = [
        "\nLet's continue with another example and infuse this function with logic.",
        "```",
        "def hack_door(code):",
        "    if code == '110799':",
        "        return 'Door unlocked.'",
        "    else:",
        "        return 'Access denied.'",
        "```",
        "This code snippet is our digital key. The `if` statement checks if the input code matches '110799'. If it does, the Matrix acknowledges our success and the door will unlock. If not, access is denied.",
        "To use this function, you call it with a potential passcode:",
        "```",
        "result = hack_door('110799')",
        "print(result)  # This prints: Door unlocked.",
        "result = hack_door('1999')",
        "print(result)  # This prints: Access denied.",
        "```"]

    wrap_and_print_text(paragraphs, width=width, delay=custom_delay)





# def link_three(name, custom_delay=0.02):
    width = get_terminal_width()
    paragraphs = [
        f"{name}, if one of our team needed you to unlock a door for them in The Matrix, you would type 'def unlock_door(code):', try it!"
    ]
    wrap_and_print_text(paragraphs, width=width, delay=custom_delay)

    while True:
        user_input = input("Type here: \n\n").strip()  #  Capture input and strip() to remove extra whitespace

        if user_input != "def unlock_door(code):":
            print_slowly("\n\nA small mistake. Remember, to define this function, type 'def unlock_door(code):'", delay=custom_delay)    ### Reword this with AI infite times?
        else:
            print_slowly("\n\nExcellent! You're one step closer to becoming a proficient operator.", delay=custom_delay)
            break




if __name__ == "__main__":
    name = get_name_from_file()
    link_ten()
    # link_three(name)


    # def reduce_string(string):
#     return string[1:len(string)-1]

# print(reduce_string("hellooo")) # DECIDE VARIABLE