import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
The one with execution and circles. Written with recursion.\n\n"""
print(introduction)


def safe_spot(n, k):
    """The first argument is the number of people standing
    on the circle. The second argument is the length of leap
    that is applied to go from one person to another. For example,
    a leap length of 1 kills people one after another, a leap
    length of 2 kills people one-in-between and so forth.
    a leap length of 0 is not acceptable as it'd make the arrow
    stuck at its place."""

    if n % k == 0 and k != 1:
        raise ValueError("\n\n\t\n\tk shouldn't divide n unless k == 1.")
    else:
        if n > k:
            return n - k
        elif k > n:
            return safe_spot(n, k - n)


print("""Go on! Switch to interactive mode and
try the safe_spot(n, k) for yourself! Help is available for
this function. Try help(safe_spot).""")
