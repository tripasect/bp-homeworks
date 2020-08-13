a = int(input("Enter your number\n> "))

def perfectQ(n):
    divisors = [1]
    for i in range(2, n - 1):
        if n % i == 0:
            divisors.append(i)
        else:
            pass
    if sum(divisors) == n:
        return True
    else:
        return False

if perfectQ(a):
    print("Yes")
else:
    print("No")

