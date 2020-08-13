import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def even_quality(n):
    if n % 2 == 0:
        return True
    else:
        return False


cls()
introduction = "This script takes in an odd number n, prints a Magic Square "
introduction += "with N = n.\n\n"
print(introduction)


while True:
    n = int(input("Enter n (length of the square). n must be odd.\n> "))
    if even_quality(n):
        cls()
        print("I said n must be ODD. Are you even listening?")
        continue
    else:
        magic_square = [[0 for x in range(n)] for y in range(n)]
        i = n / 2
        j = n - 1
        num = 1
        while num <= (n * n):
            if i == -1 and j == n:
                j = n - 2
                i = 0
            else:
                if j == n:
                    j = 0
                if i < 0:
                    i = n - 1
            if magic_square[int(i)][int(j)]:
                j = j - 2
                i = i + 1
                continue
            else:
                magic_square[int(i)][int(j)] = num
                num = num + 1
            j = j + 1
            i = i - 1
        print ("Magic Square for N =", n)
        print ("Magic Sum =", int(n * (n * n + 1) / 2), "\n")
        for i in range(0, n):
            for j in range(0, n):
                print("{:^7}".format(str(magic_square[i][j])), end = '')
                if j == n - 1:
                    print()
        input("\nPress [ENTER] for another round.\n")
        cls()
