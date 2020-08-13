import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = "This script takes in a number and yields its prime factors.\n\n"
print(introduction)


def prime_quality(n):
    """Returns True if n is prime and False otherwise. 1 is not prime."""
    if n == 1:
        return False
    else:
        pass
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    else:
        return True


def primes_less_than(n):
    """Returns all primes less than its input as a list."""
    result = []
    for i in range(2, int(n)):
        if prime_quality(i):
            result.append(i)
        else:
            pass
    return result


def prime_factors(n):
    """Returns all prime factors of n as a list. repeating factors are
    appended in the list for multiple times."""
    result = []
    suspects = primes_less_than(n + 1)
    for suspect in suspects:
        while n % suspect == 0:
            result.append(suspect)
            n /= suspect
    return result


while True:
    prompt = "\nEnter your number.\n> "
    a = int(input(prompt))
    print(f"The prime factors of {a} are:")
    print(prime_factors(a))
    prompt = "Press [ENTER] for another round.\n"
    input(prompt)
    cls()
