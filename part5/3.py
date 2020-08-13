import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
The one with reordering numbers such that
the more left a number is the less difference
it has with its neighbors and its difference
with its __left__ neighbor is even less than
its difference with its __right__ neighbor.\n"""
print(introduction)

while True:
    n = input("Enter n.\n--This input is unnecessary. "
              "Press [ENTER] to skip.--\n> ")
    # why should we even ask for n when we're
    # getting the members themselves?! Well, I'm not using this variable.

    numbers = input("\nEnter numbers subsequently, "
                    "separated by space.\n> ")
    numbers = [int(number) for number in numbers.split()]

    # this is how you do it and you don't even do it
    # n = len(numbers)

    ordered = [numbers[0]]
    del numbers[0]

    for j in range(len(numbers)):
        a = numbers[0]
        d = abs(ordered[-1] - numbers[0])
        j += 1
        for number in numbers:
            if abs(ordered[-1] - number) < d:
                a = number
                d = abs(ordered[-1] - number)
            else:
                pass
        ordered.append(a)
        numbers.remove(a)

    print(f"\nThe list goes as:\n>> {ordered}")

    input("\nPress [ENTER] for one more hand.\n")
    cls()
