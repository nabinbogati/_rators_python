"""
    builtin function:

    zip(*iterables):
        takes 2 or more iterables and returns a tuple
        contaning the elements from * iterables

    filter(function, iterable):
        filter outs iterables using conditional statements in fucnction

    reduce(function, iterable):
        reduce iterables to return cummulative value

    map(function, iterables):
        reurns iterable (list) by performing on function with iterable
"""

from functools import reduce


# zip
def zip_fun(key, value):
    return zip(tup1, tup2)


# filter
def filter_even(value):
    return value%2 == 0

def filter_odd(value):
    return value%2 != 0


# reduce
def reduce_sum(ret, y):
    return ret+y

def reduce_mul(ret, y):
    return ret*y


# _map
def compute_square(value):
    return value*value

def compute_multiple(val1, val2):
    return val1*val2


if __name__ == '__main__':
    tup1 = (1, 2, 3, 4, 5)
    tup2 = (1, 4, 9, 16, 25)
    numbers = range(1, 20)

    # zip
    _zip = zip_fun(tup1, tup2)
    __zip = zip_fun(tup1, tup2)
    print("zip: ", _zip, __zip)

    # filter
    _even = filter(filter_even, numbers)
    _odd = filter(filter_odd, numbers)
    print("zip: ", _even, _odd)

    # reduce
    _reduce = reduce(reduce_sum, numbers)
    __reduce = reduce(reduce_mul, numbers)
    print("reduce: ", _reduce, __reduce)

    # map
    _map = list(map(compute_square, tup1))
    __map = list(map(compute_multiple, tup1, tup2))
    print("map: ", _map, __map)
