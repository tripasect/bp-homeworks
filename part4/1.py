import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
This script has a function that can convert hexadecimals (as string)
to decimals. The code is written manually rather than with builtin
Python methods.\n\n"""
print(introduction)


print("""Go on! Switch to interactive mode and
try the hex_to_dec(str) for yourself!""")


def hex_to_dec(str):
    extras = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
              'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    if str[0] == '-':
        return (-1 * hex_to_dec(str[1:]))
    else:
        dec = 0
        l = 0 # array from left
        r = -1 # array from right
        for i in range(len(str)):
            # if the character lies in (0, 9)
            try:
                int(str[r])
                dec += int(str[r]) * (16 ** l)
                l += 1
                r -= 1
            # if the character lies in (a, f)
            except ValueError:
                dec += extras[str[r]] * (16 ** l)
                l += 1
                r -= 1
        return dec


## NOTE: Below piece of code works too. I assumed that is too hooloo_too_galoo
## so I avoided it.

# def builtin_hex_to_dec(str):
#     print(int(str, 16))
