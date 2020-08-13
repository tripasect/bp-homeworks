import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """This script takes in a base length and a height length
and prints some bullshit parallelograms with that base and that height.\n\n"""
print(introduction)


while True:
    prompt = "Enter the the length of the base of the parallelogram.\n> "
    b = int(input(prompt))
    prompt = "Enter the the length of the height of the parallelogram.\n> "
    h = int(input(prompt))
    cls()
    spaces = ''
    for i in range(h):
        spaces += ' '
        print(b * '*', sep=' ', end='\n' + spaces)
    input('\rPress Enter for another round.')
    cls()
