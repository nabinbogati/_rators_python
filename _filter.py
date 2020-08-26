"""
    python builtins for filtering out from iterables

    returns filtered out iterable

    filter(function, iterable)

"""


def filter_even(value):
    return value%2 == 0


def filter_odd(value):
    return value%2 != 0


if __name__ == '__main__':
    numbers = range(20)

    even_numbers = filter(filter_even, numbers)
    print(list(even_numbers))

    odd_numbers = filter(filter_odd, numbers)
    print(list(odd_numbers))
