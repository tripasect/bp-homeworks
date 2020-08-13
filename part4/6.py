import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
Matrix Power Raiser 2000. Uses recursion.\n\n"""
print(introduction)


def identity(n):
    "Returns the identity matrix with N = n."
    mat = []
    for row in range(n):
        mat.append([0 for j in range(n)])
    column = 0
    for row in mat:
        row[column] = 1
        column += 1
    return mat


def multiply(matA, matB):
    "Multiplies its first argument--a mat--in its second argument--a mat."
    zip_b = list(zip(*matB)) # this makes rows columns and columns rows in matB
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in matA]


def power(mat, n):
    "Raises its first argument--a matrix--to its second argument--an integer."
    if n == 0:
        return identity(len(mat))
    elif n % 2 == 0:
        return multiply(power(mat, n / 2), power(mat, n / 2))
    else:
        alpha = multiply(power(mat, int(n / 2)), power(mat, int(n / 2)))
        return multiply(alpha, mat)


def show(mat):
    max_length = 0
    for row in mat:
        print(row)
    print('')


print("""
Go on. Switch to interactive mode and use
power(mat, n) function to raise your
matrix to the power of n. You can also
use show(power(mat, n)) to have a more
intuitive printing format.

    Your matrix should always be
a list of lists. for example,
A 1x1 matrix will be passed in
as a list of a 1-element list.\n""")

#TrIpasect9okn2wsx
