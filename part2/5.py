import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
introduction = "This script takes in a matrix as a string and says which "
introduction += "element in where is the maximum element.\n\n"
print(introduction)


while True:
    prompt = "Pass in your 4x4 Matrix in linear form seperated by white spaces."
    prompt += "\nExample: 4 5 9 6\n\n> "
    matrix = [int(element) for element in input(prompt).split(' ')]
    for i in range(4):
        if matrix[i] == max(matrix):
            print(f"{max(matrix)} at {i + 1}")
        else:
            pass
    input("Press [ENTER] for another round.")
    cls()
