import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
The one with employees and files and info.txt, etcetera, etcetera.\n"""
print(introduction)


file = open("info.txt")
records = [record.strip() for record in file.readlines()]
people = []
for record in records:
    split = record.split()
    dictionary = {}
    dictionary['name'] = split[0]
    dictionary['surname'] = split[1]
    dictionary['age'] = split[2]
    dictionary['history'] = split[3]
    people.append(dictionary)


def original_format(dic):
    "Converts my dictionary to the original format."
    str = ''
    str += dic['name'] + ' '
    str += dic['surname'] + ' '
    str += dic['age'] + ' '
    str += dic['history'] + '\n'
    return str


def is_valid(dic):
        "Returns True if the record is valid, False othewise."
        checklist = []

        # name verification
        if dic['name'] != 'NULL':
            if len(dic['name']) >= 2 and len(dic['name']) <= 32:
                checklist.append(True)
            else:
                checklist.append(False)
        else:
            checklist.append(True)
        # done

        # surname verification
        if dic['surname'] != 'NULL':
            if len(dic['surname']) >= 4 and len(dic['surname']) <= 64:
                checklist.append(True)
            else:
                checklist.append(False)
        else:
            checklist.append(True)
        # done

        # age verification
        if dic['age'] != 'NULL':
            if int(dic['age']) >= 18 and int(dic['age']) <= 99:
                checklist.append(True)
            else:
                checklist.append(False)
        else:
            checklist.append(True)
        # done

        # history verification
        if dic['history'] != 'NULL':
            if int(dic['history']) >= 0 and int(dic['history']) <= 240:
                checklist.append(True)
            else:
                checklist.append(False)
        else:
            checklist.append(True)
        # done

        return all(checklist)


file1 = open("1.txt", 'w')
for person in people:
    if person['age'] == '21':
        file1.write(original_format(person))
    else:
        pass
file1.close()


file2 = open("2.txt", 'w')
for person in people:
    if person['age'] != 'NULL':
        if int(person['age']) > 40:
            file2.write(original_format(person))
        else:
            pass
    else:
        pass
file2.close()


file3 = open("3.txt", 'w')
for person in people:
    if person['age'] != 'NULL' and person['history'] != 'NULL':
        if int(person['age']) > 25 and int(person['history']) < 12:
            file3.write(original_format(person))
        else:
            pass
    else:
        pass
file3.close()


file4 = open("4.txt", 'w')
for person in people:
    if person['name'] == 'ali':
            file4.write(original_format(person))
    else:
        pass
file4.close()


file5 = open("5.txt", 'w')
for person in people:
    if 'amir' in person['name']:
            file5.write(original_format(person))
    else:
        pass
file5.close()


file6 = open("6.txt", 'w')
for person in people:
    if 'mohammad' in person['name'] and len(person['surname']) < 4:
            file6.write(original_format(person))
    else:
        pass
file6.close()


file7 = open("7.txt", 'w')
for person in people:
    if not is_valid(person):
            file7.write(original_format(person))
    else:
        pass
file7.close()


file8 = open("8.txt", 'w')
for person in people:
    if person['name'] == 'mahdi' and is_valid(person):
            file8.write(original_format(person))
    else:
        if person['age'] != 'NULL' and is_valid(person):
            if int(person['age']) < 21:
                file8.write(original_format(person))
            else:
                pass
        else:
            pass
file8.close()


file9 = open("9.txt", 'w')
for person in people:
    try:
        if int(person['age']) < 30 and\
        int(person['history']) > 24 and\
        'ali' in person['name'] and\
        is_valid(person):
           file9.write(original_format(person))
        else:
            pass
    except ValueError:
        pass
file9.close()


file10 = open("10.txt", 'w')
list10 = []
for person in people:
    if person['name'] == 'ali' and is_valid(person):
            list10.append(tuple(person.values()))
    else:
        pass
    list10.sort(key = lambda x: x[1])
for person in list10:
    string = ''
    string += person[0] + ' '
    string += person[1] + ' '
    string += person[2] + ' '
    string += person[3] + '\n'
    file10.write(string)
file10.close()


file11 = open("11.txt", 'w')
list11 = []
for person in people:
    if 'hassan' in person['surname'] and is_valid(person):
        list11.append(list(person.values()))
    else:
        if person['age'] != 'NULL' and is_valid(person):
                if int(person['age']) < 25:
                    list11.append(list(person.values()))
                else:
                    pass
        else:
            pass

list11_null = []
list11_not_null = []

for record in list11:
    if record[3] != 'NULL':
        list11_not_null.append(record)
    else:
        list11_null.append(record)

for record in list11_not_null:
    record[3] = int(record[3])

list11_not_null.sort(key = lambda x: x[3])

for record in list11_not_null:
    string = ''
    string += record[0] + ' '
    string += record[1] + ' '
    string += record[2] + ' '
    string += str(record[3]) + '\n'
    file11.write(string)

for record in list11_null:
    string = ''
    string += record[0] + ' '
    string += record[1] + ' '
    string += record[2] + ' '
    string += record[3] + '\n'
    file11.write(string)

file11.close()
