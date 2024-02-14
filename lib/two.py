from main import get_terminal_width

## Training Program
## Create Function 

def first_function():
    text = "Create a function that removes the first and last characters of a string. You have the use of one parameter, the original string. Don't worry about strings with less than two characters\n"
    # print_slowly(text, delay=0.075)
    print(text)

get_terminal_width()
first_function()

def reduce_string(string):
    return string[1:len(string)-1]

print(reduce_string("hellooo"))

## Have a file containing tests. Potentially unittests at bottom of file. File def if necc. User writes code. 