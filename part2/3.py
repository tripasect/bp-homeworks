import os
from math import factorial


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = "This script takes in a number, say, n, and prints the "
introduction += "Pascal Triangle up to nth row.\n\n"
print(introduction)


def combination(r, n):
    return factorial(n) / (factorial(r)*factorial(n - r))



while True:
    pascals_triangle = []
    prompt = "To what row do you want your Pascal Triangle to be printed?\n> "
    row_count = int(input(prompt))
    for row in range(row_count + 1):
        result = [int(combination(i, row)) for i in range(row + 1)]
        pascals_triangle.append(result)
    cls()
    for row in pascals_triangle:
        for number in row:
            print("{:^5}".format(number), end=' ')
        print('')
    prompt = "\nPress [ENTER] for another round.\n"
    input(prompt)
    cls()
