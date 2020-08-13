import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
introduction = """\tINTRODUCTION:
A function that has a dictionary argument. It spits a dictionary containig only
those items of the input dictionary that have unique values.
Go to interactive mode and use only_unique_values(dic).\n"""
print(introduction)


def only_unique_values(dic):
    """
    for example,
    if
    dic = {"Newton": "gravity",
           "Sandra Bullock": "gravity",
           "Einstein": "relativity"}
    then the output will be
    {"Einstein": "relativity"}.
    (Because "gravity" isn't unique among all values, but "relativity" is.)
    """
    result = {}
    for key,value in dic.items():
      if list(dic.values()).count(value) == 1:
          result[key] = value
      else:
          pass
    return result
