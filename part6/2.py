import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
A function that spits a sort of intersection of two dictionaries.
Go to interactive mode and use intersection_of_dictionaries(dic1, dic2).\n"""
print(introduction)


def intersection_of_dictionaries(dic1, dic2):
    """
    for example,
    if dic1 = {"gravity": "Newton", "relativity": "Einstein"}
    and dic2 = {"gravity": "Sandra Bullock", "relativity": "Einstein"},
    then the output will be
    {"relativity": "Einstein"}.
    """
    dic = {}
    for key in dic1.keys():
        if key in dic2.keys():
            if dic1[key] == dic2[key]:
                dic[key] = dic1[key]
            else:
                pass
        else:
            pass
    return dic
