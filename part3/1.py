import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
This script gets in a string and tells you whether it is a palindrome or not.
prints True for palindrome and False for not palindrome.
The empty string and strings with the length of 1 are considered palindromes.\n\n"""
print(introduction)


def palindrome_quality(string):
    list = [char for char in string]
    list_copy = list[:]
    list.reverse()
    if list_copy == list:
        return True
    else:
        return False

while True:
    prompt = "Pass in your string, kind sweetheart.\n> "
    string = input(prompt)
    print(palindrome_quality(string))
    prompt = "\nPress [ENTER] for one more hand.\n"
    input(prompt)
    cls()
