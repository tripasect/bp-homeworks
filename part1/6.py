a = int(input("Enter the 1st number.\n> "))
b = int(input("Enter the 2nd number.\n> "))
c = int(input("Enter the 3rd number.\n> "))

# max
if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c
# min
if a < b:
    if a < c:
        min = a
    else:
        min = c
else:
    if b < c:
        min = b
    else:
        min = c

print(f"MAX = {max}")
print(f"MIN = {min}")