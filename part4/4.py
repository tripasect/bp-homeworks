import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
Decides if a string is a palindrome or not. Uses recursion.\n\n"""
print(introduction)


def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False


while True:
    prompt = "Enter you word.\n> "
    word = input(prompt)
    print(is_palindrome(word))
    input("Press [ENTER] for one more hand.\n")
    cls()
