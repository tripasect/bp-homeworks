import os
from math import factorial, pi # for Taylor series and
                               # for taking out 2 * Pi's from x.

from math import sin as sine, cos as cosine # just for comparing
# from math import cos as cosine # just for comparing

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
This script, takes in two numbers; n and x. If n == 0, it prints
sine of x and if else, it prints cosine of x. Results are accurate to
4 digits and the calculation method is based on Taylor series.\n\n"""
print(introduction)


def sin(x):
    x = x % (2 * pi)
    result = 0
    i = 0
    while (x**(2 * i + 1)) / factorial(2 * i + 1) > 0.000001:
        result += ((-1)**i) * (x**(2 * i + 1)) / factorial(2 * i + 1)
        i += 1
    return round(result, 4)


def cos(x):
    x = x % (2 * pi)
    result = 0
    i = 0
    while (x**(2 * i)) / factorial(2 * i) > 0.000001:
        result += ((-1)**i) * (x**(2 * i)) / factorial(2 * i)
        i += 1
    return round(result, 4)

while True:
    prompt = """Enter the number n. If n == 0, sin and if else,
cos will be calculated.\n> """
    n = input(prompt)
    print('\nSIN' if n == '0' else '\nCOS', 'it is!')
    prompt = """Enter the number x
(this number will be the argument of the function).\n> """
    x = float(input(prompt))


    if n == '0':
        print("\t My sin:\n\t", sin(x), '\n')
        print("\t Built-in sin:\n\t", sine(x))
    else:
        print("\t My cos:\n\t", cos(x), '\n')
        print("\t Built-in cos:\n\t", cosine(x))

    input('\nPress [ENTER] for one more hand!\n')
    cls()
