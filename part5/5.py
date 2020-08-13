import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
The one with artifacts and natural disasters.\n"""
print(introduction)


while True:
    n = input("Enter n.\n--This input is unnecessary. "
              "Press [ENTER] to skip.--\n> ")
    # why should we even ask for n when we're
    # getting the members themselves?! Well, I'm not using this variable.

    count = 0

    numbers_as_string = input("\nEnter the n numbers on the artifact "
                              "subsequently, separated by space.\n> ")
    numbers = [int(member) for member in numbers_as_string.split()]

    if 1 not in numbers:
        count += 1

    if 1000 not in numbers:
        count += 1

    numbers.sort()

    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] > 1:
            count += 1
        else:
            pass

    print(f"\nThe minimum count of disasters is:\n>> {count}")

    input("\nPress [ENTER] for one more artifact!\n")
    cls()
