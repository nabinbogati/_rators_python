""" iterators are always being used implictly in collection types:
    List, Tuple, String.
    The general usual method for traversing a collection is using loops which inplictly uses the iter method that receives an iterable and returns an iterator object. 
    iterator.__next__() or next(iterator)
    """


# using loop to traverse collection

iterable = [1, 2, 3, 4, 5]
def using_loops(iterable):
    for item in iterable:
        print(item)


def using_iterator(iterable):
    iterator = iter(iterable)

    while True:
        try:
            item = next(iterator)
            print(item)
        except StopIteration:
            break


if __name__ == '__main__':
    using_loops(iterable)

    using_iterator(iterable)
