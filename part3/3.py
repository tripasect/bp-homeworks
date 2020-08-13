import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
The program gets two strings from user. It then removes characters of the second
string that are available in the first string.\n\n"""
print(introduction)

while True:
    string = input("Enter your main string.\n> ")
    prompt = """\nEnter the set of letters you wish to
be erased from the main string.\n> """
    bite = input(prompt)
    final = ''
    for char in string:
        if char in bite:
            pass
        else:
            final += char
    print("\nThere you go:\n", final, sep='')
    input("\nPress [ENTER] for one more hand.\n")
    cls()
