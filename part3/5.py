import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def ordinal(num):
    """Returns ordinal number string from int,
    e.g. 1, 2, 3 becomes 1st, 2nd, 3rd, etc."""

    n = int(num)
    if 4 <= n <= 20:
      suffix = 'th'
    elif n == 1 or (n % 10) == 1:
      suffix = 'st'
    elif n == 2 or (n % 10) == 2:
      suffix = 'nd'
    elif n == 3 or (n % 10) == 3:
      suffix = 'rd'
    elif n < 100:
      suffix = 'th'
    ord_num = str(n) + suffix
    return ord_num


cls()
introduction = """\tINTRODUCTION:
Takes a number n and then asks for n name-ages. Sorts by name, if had the
same name the person with smaller age comes first.\n\n"""
print(introduction)


while True:
    n = int(input("Enter the n. AKA the number of your coming inputs.\n> "))
    people = []
    for i in range(n):
        prompt = f"\nPass in the string associated with your {ordinal(i + 1)} character.\n> "
        person = input(prompt).split(' ')
        person[1] = int(person[1])
        people.append(person)

    people.sort()

    # When Turing Cried, Chapter 7
    for j in range(len(people)):
        for i in range(len(people)):
            try:
                if (people[i][0] == people[i + 1][0]) and (people[i][1] > people[i + 1][1]):
                    # above line: if two adjacent people had the same name and
                    # were placed incorrectly, they get reordered
                    people[i], people[i + 1] = people[i + 1], people[i]
            except IndexError:
                pass

            else:
                pass


    print("\n")
    for person in people:
        print(person[0], person[1])
    input("\nPress [ENTER] for one more hand.\n")
    cls()
