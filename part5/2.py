import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
The one with face masks and stores.\n"""
print(introduction)

while True:
    n = input("Enter n.\n--This input is unnecessary. "
              "Press [ENTER] to skip.--\n> ")
    # why should we even ask for n when we're
    # getting the members themselves?! Well, I'm not using this variable.

    prices = input("\nEnter prices subsequently, "
                   "separated by space.\n> ")
    prices = [int(price) for price in prices.split()]

    money = float(input("\nEnter the amount of money he possesses.\n> "))

    # the count of stores he can buy face mask from
    count = 0
    for price in prices:
        if price <= money:
            count += 1
        else:
            pass

    print(f"\nThe number of stores he can buy from is:\n>> {count}")

    input("\nPress [ENTER] for one more hand.\n")
    cls()