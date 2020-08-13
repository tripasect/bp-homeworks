import os
from math import ceil


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
An increasing list of length n goes in, such that every member is
repeated twice except one. This script finds that member in
logarithmic time.\n"""
print(introduction)


def even(m):
    if m % 2 == 0:
        return True
    else:
        return False


def odd(m):
    if m % 2 == 1:
        return True
    else:
        return False


def before_at_after(k, list):
    try:
        if even(k) and list[k] == list[k - 1]:
            return 1
        # arrow is after target

        elif odd(k) and list[k] == list[k + 1]:
            return 1
        # arrow is after target

        elif odd(k) and list[k] == list[k - 1]:
            return 0
        # arrow is before target

        elif even(k) and list[k] == list[k + 1]:
            return 0
        # arrow is before target

        else:
            return 0.5
        # arrow is at target

    except IndexError:
        return 0.5
    # to handle the case in which the target is at the ending points.
    # (k + 1 / k - 1 wouldn't exist and IndexError would raise, so,
    # that for that.)


while True:
    n = input("Enter n.\n--This input is unnecessary. "
              "Press [ENTER] to skip.--\n> ")
    # why should we even ask for n when we're
    # getting the members themselves?! Well, I'm not using this variable.

    numbers = input("\nEnter your n numbers subsequently, "
                    "separated by space.\n> ")

    numbers = [int(member) for member in numbers.split()]
    # n = len(prices)

    H = len(numbers)
    L = 0

    # pivot index
    M = ceil((H + L) / 2)
    coordination = before_at_after(M, numbers)
    # coordination would show where we're at in relation to target
    # 0: before it, 0.5: at it, 1: after it

    while coordination != 0.5:
        if coordination == 0:
            L = M
            M += ceil((H - M) / 2)
            coordination = before_at_after(M, numbers)
        else:
            H = M
            M -= ceil(M / 2)
            coordination = before_at_after(M, numbers)

    print(f"\nThe single repeated number is:\n>> {numbers[M]}")

    input("\nPress [ENTER] for one more hand.\n")
    cls()

