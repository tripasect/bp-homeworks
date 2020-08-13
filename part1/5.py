from math import sin
from math import pi

a = float(input("Length of the 1st edge of the triangle.\n> "))
b = float(input("Length of the 2nd edge of the triangle.\n> "))
C = float(input("""Size of the angle of the triangle that
resides between the 1st edge and the 2nd edge (degrees).\n> """))

S = a * b * 0.5 * sin(pi * C / 180)
print(S)
