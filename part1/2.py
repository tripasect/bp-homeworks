a = int(input("Enter the 1st number.\n> "))
b = int(input("Enter the 2nd number.\n> "))

def GCF(a, b):
    if a*a + b*b == 0:
        raise ZeroDivisionError
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return GCF(min(a, b), max(a, b) - min(a, b))

def LCM(a, b):
    return int(a * b / GCF(a, b))

print(LCM(a, b))