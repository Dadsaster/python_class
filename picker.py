import random

def picker(list):
    list_out = []
    list_in = list[:]
    while list:
        pick = random.choice(list)
        list_out.append(pick)
        index = list.index(pick)
        list.pop(index)
    print(dict(zip(list_in, list_out)))


list = ['a', 'b', 'c', 'd', 'e']
print(picker(list))