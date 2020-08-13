import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = "This script takes in a number and prints its /MAGHLOOB/.\n\n"
print(introduction)


def list_to_string(l):
    """Takes a list. Yields a string version of that list."""
    result = ''
    for element in l:
        result += str(element)
    return result


def string_to_list(s):
    """Takes a string. Yields a list version of that string."""
    result = []
    for character in s:
        result.append(character)
    return result


def reverse(l):
    """Takes a list. Yields the reverse of that list."""
    l.reverse()
    return l

while True:
    prompt = "Enter your number.\n> "
    number_as_string = input(prompt)
    number_as_list = string_to_list(number_as_string)
    number_as_list_reversed = reverse(number_as_list)
    number_as_string_reversed = list_to_string(number_as_list_reversed)
    number_as_integer_reversed = int(number_as_string_reversed)
    print(number_as_integer_reversed)
    input("Press [ENTER] for another round.")
    cls()
