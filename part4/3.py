import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
Give a string in, it gives out all its anagrams
as a list. It's written using recursion.\n\n"""
print(introduction)


def anagrams(word):
    if len(word) == 1:
        return word
    else:
        results = []
        for anagram in anagrams(word[1:]):
            for i in range(len(word)):
                results.append(anagram[:i] + word[0:1] + anagram[i:])
        return list(set(results))


while True:
    prompt = "Enter you word.\n> "
    word = input(prompt)
    print((anagrams(word)))
    input("Press [ENTER] for one more hand.\n")
    cls()
