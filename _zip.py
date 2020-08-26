"""
    builtin function that takes 2 or more iterables and returns a tuple
    contaning the elements from * iterables

    zip(*iterables)

"""


def mappings(key, value):
    return zip(tup1, tup2)



if __name__ == '__main__':
    tup1 = (1, 2, 3, 4, 5)
    tup2 = (1, 4, 9, 16, 25)

    maps = mappings(tup1, tup2)
    print(list(maps))

    mappings = mappings(tup1, tup2)
    print(dict(mappings))
