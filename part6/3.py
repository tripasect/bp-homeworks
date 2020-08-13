import os
from random import sample

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
A function that spits 3 random integers from 1 up to its integer argument n,
in a way that no 2 of them are consecutive.
Go to interactive mode and use random3(n).\n"""
print(introduction)

def random3(n):
    universe = list(range(1, n + 1))
    final = []

    # picking a 1-member sample and then removing its neighbors from universe
    final += list(sample(universe, 1))
    try:
        universe.remove(final[0] + 1)
    except ValueError:
        pass
    try:
        universe.remove(final[0] - 1)
    except ValueError:
        pass

    # picking a 1-member sample and then removing its neighbors from universe
    final += list(sample(universe, 1))
    try:
        universe.remove(final[1] + 1)
    except ValueError:
        pass
    try:
        universe.remove(final[1] - 1)
    except ValueError:
        pass

    # picking a final member
    final += list(sample(universe, 1))

    return final
