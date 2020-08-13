import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
Has a function scalar_mult(s, v). Takes a scalar and a list, multiplies
all the members of the list in the scalar and prints the new list.\n\n"""
print(introduction)


def scalar_mult(s, v):
    return [s * m for m in v]

print("""Go on! Switch to interactive mode and
try the scalar_mult(s, v) for yourself!""")
