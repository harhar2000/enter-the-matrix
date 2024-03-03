from common import *

def enter_name(custom_delay=0.075):
    prompt = "Enter Name: "
    print_slowly(prompt, delay=custom_delay)
    name = input()
    
    greeting = f"\nWake up, {name}\n\n" + "The Matrix has you... \n\n\n"
    print_slowly(greeting, delay=custom_delay)

    link_welcome(name, custom_delay=0.02)
    return name

def link_welcome(name, custom_delay=0.02):
    width = get_terminal_width()
    paragraphs = [
        f"Hey {name}, I'm Link. As Operators, we're the mission control for crew inside the Matrix. We provide support from navigation to technical hacks, ensuring the team has everything they need for their missions.",
        "Your role is to guide them through the Matrix, monitoring for threats and hacking systems to stay ahead of our enemies. We manipulate the code to assist our crew, whether that's unlocking doors or accessing crucial data.",
        "I'll teach you to upload knowledge directly to their minds. They need to know Kung Fu or how to fly a helicopter? You'll have them covered.",
        "Though we might not be on the frontline our expertise and support is indispensable. We're their eyes and ears, backing them up every step of the way.",
        "Type 'python two.py' into your console to activate your first training program.",
        " "
    ]

    wrap_and_print_text(paragraphs, width=width, delay=custom_delay)


if __name__ == "__main__": 
    name = enter_name()
    with open("namefile.txt", "w") as file:
        file.write(name)