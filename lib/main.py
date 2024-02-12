import time
import textwrap
import os

def print_slowly(text, delay=0.075): # Prints text slowly, character by character
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_terminal_width(default=70):
    try:
        columns, _ = os.get_terminal_size()
        return columns
    except OSError:
        return default

def enter_the_matrix(custom_delay=0.075):
    prompt = "Enter Name: "
    print_slowly(prompt, delay=custom_delay)
    name = input()
    
    greeting = f"\nWake up, {name}\n\n" 
    message = "The Matrix has you..."
    
    print_slowly(greeting, delay=custom_delay)
    print_slowly(message, delay=custom_delay)
    link_welcome(name, custom_delay=0.02)

def link_welcome(name, custom_delay=0.02):
    width = get_terminal_width() 
    paragraphs = [
        f"\n\n\nHey {name}, I'm Link, nice to have you onboard. As Operators, we're the mission control for our crew inside the Matrix. We provide real-time support, from navigation to technical hacks, ensuring the team has everything they need for their missions.",
        "Our role encompasses guiding through the Matrix, monitoring for threats and hacking systems to stay ahead of our enemies. We manipulate the Matrix's code to assist our crew, whether that's unlocking doors or accessing crucial data.",
        "I'll teach you to instantly upload knowledge directly to our team's minds. They need to know Kung Fu or how to fly a helicopter? We have them covered.",
        "When situations escalate, we coordinate extractions: finding the nearest exit points to pull our team out safely. We also manage the inventory of weapons and tools, ensuring our team have everything and anything they need.",
        "Though we might not be on the frontline, our expertise and support are indispensable. We're their eyes and ears, keeping them connected, guided and backed up every step of the way. Without us, there's no bridge to the real world or the vital support our rebels rely on."
    ]

    wrapped_text = '\n\n'.join([textwrap.fill(paragraph, width=width) for paragraph in paragraphs]) # Wrap each paragraph to fit terminal and join with double newlines

    print_slowly(wrapped_text, delay=custom_delay)

enter_the_matrix()
