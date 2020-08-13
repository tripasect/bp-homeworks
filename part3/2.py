import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
The weird program with bombs and whatnot.\n\n"""
print(introduction)


def tuple_string_to_list(str):
    """Gets in an unordered string of the form "(21,armin,(5,6))" and converts
    it to an ordered list with name (as string), age (as int), and coordinates
    (as tuple) in it, respectedly."""

    alphabet = [chr(int) for int in range(65, 91)] # caps
    alphabet += [chr(int) for int in range(97, 123)] # small-case

    body = str[1:-1] # cuts the two parantheses at the two ends
    list_primal = body.split(',') #['21', 'armin', '(5', '6)']

    list_without_the_coordinates = [] # I add the age and the name, the
    # coordinates are a little more complicated so I postpone them until the
    # last moment


    # below procedure appends the age and the name respectedly

    # appending the name
    for member in list_primal:
        for letter in alphabet:
            if letter in member:
                list_without_the_coordinates.append(member.strip())
                break

    # appending the age
    for member in list_primal:
        try:
            int(member)
            list_without_the_coordinates.append(int(member))
        except ValueError:
            pass

    # appending the coordinates
    open_paran = 1 # an arrow to find where the open-paranthesis is
    close_paran = 0 # an arrow to find where the close-paranthesis is

    for i in range(len(body)): # a for-loop to locate the open_paranthesis
        if body[i:i+1] == '(':
            break
        else:
            open_paran += 1

    for j in range(len(body)): # a for-loop to locate the close_paranthesis
        if body[j:j+1] == ')':
            break
        else:
            close_paran += 1

    list = list_without_the_coordinates # the final list. I'm finalizing the work

    list.append(tuple(map(float, body[open_paran:close_paran].split(','))))
    # in above line I appended the coordinates to the previous list as a tuple

    # done
    return list


def within_range(A, B, k):
    """Returns True if point A is k units or less away from point B.
    False if otherwise. A and B are two-tuples and k is a float."""

    if ((A[0] - B[0])**2 + (A[1] - B[1])**2)**0.5 <= k:
        return True
    else:
        return False


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


def str_to_tuple(string):
    """Gets in a two-tuple in the form of a string.
    Takes it in in tuple form."""

    string = string[1:-1]
    comma_position = 0
    for char in string:
        if char == ',':
            break
        else:
            comma_position += 1

    return (float(string[:comma_position]), float(string[comma_position + 1:]))


while True:
    nk = input("""Pass in the n and the k, respectedly. (Seperate the two numbers
with a single comma character.)\n> """)
    nk = list(map(float, nk.split(','))) # converting it to a list of floats.


    people = [] # an empty list to put our people into

    for i in range(int(nk[0])): # nk[0] is n. nk[1] is k.
        prompt = f"""\nEnter the 3-tuple associated with your
{ordinal(i + 1)} person. (Seperate items with a single comma character.)\n> """
        person_string = input(prompt) # gets the  character-string from user
        people.append(tuple_string_to_list(person_string)) # appends the converted version
        # to our list of people

    bomb = input("\nWhere is the bomb? [EXAMPLE: (0,0)]\n> ")

    survivors = []
    for person in people:
        if not within_range(person[2], str_to_tuple(bomb), nk[1]):
            # person[2] is person's coordinates, str_to_tuple(bomb) is just
            # the coordinates of the bomb and nk[1] is k which is the range.
            survivors.append(person)
        else:
            "dead :("


    survivors.sort()
    print("Below people survived, hooff.")
    print(survivors)
    input("\nPress [ENTER] for one more hand.\n")
    cls()
