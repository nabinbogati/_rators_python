"""
    python builtin map function

    map takes a function as a first argument and iterable as other argument
    (one or many) and returns an iterable (list)

"""
def compute_square(value):
    return value*value

def compute_multiple(val1, val2):
    return val1*val2


if __name__ == '__main__':
    tup1 = (1, 2, 4, 5, 6, 9, 8)
    tup2 = (2, 4, 6, 8, 10, 12, 14)


    result1 = list(map(compute_square, tup1))
    print(result1)

    result2 = list(map(compute_multiple, tup1, tup2))
    print(result2)
