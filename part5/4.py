import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
The one with boards and the two who play on it.\n"""
print(introduction)


while True:
    n = input("Enter n.\n--This input is unnecessary. "
              "Press [ENTER] to skip.--\n> ")
    # why should we even ask for n when we're
    # getting the members themselves?! Well, I'm not using this variable.

    numbers = input("\nEnter the n numbers on the board "
                    "subsequently, separated by space.\n> ")

    numbers = [int(member) for member in numbers.split()]

    numbers_decreasing = sorted(numbers)
    numbers_increasing = sorted(numbers, reverse=True)

    i = 0
    while len(numbers) > 1:
        numbers.remove(numbers_increasing[i])
        if len(numbers) > 1:
            numbers.remove(numbers_decreasing[i])
        i += 1

    print(f"\nThe remaining last number is:\n>> {numbers[0]}")

    input("\nPress [ENTER] for one more hand.\n")
    cls()
