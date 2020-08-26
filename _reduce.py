"""
    python defined in functools for reducing out iterables

    returns single cummulative value

    reduce(function, iterable)

"""
from functools import reduce


def reduce_sum(ret, y):
    return ret+y


def reduce_mul(ret, y):
    return ret*y


if __name__ == '__main__':
    numbers = range(1, 20)

    total = reduce(reduce_sum, numbers)
    print(total)

    product = reduce(reduce_mul, numbers)
    print(product)

