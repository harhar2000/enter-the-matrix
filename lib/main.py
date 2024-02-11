import time

def print_slowly(text, delay=0.075):
    """Prints the given text, one character at a time, with a delay between each character."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def enter_the_matrix(custom_delay=0.075):
    prompt = "Enter Name: "
    print_slowly(prompt, delay=custom_delay)
    name = input()
    
    greeting = f"\nWake up, {name}\n\n" 
    message = "The Matrix has you..."
    
    print_slowly(greeting, delay=custom_delay)
    print_slowly(message, delay=custom_delay)

enter_the_matrix()
