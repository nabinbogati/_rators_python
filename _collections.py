"""
    implements specialized container datatypes providing
    alternative to Python's general purpose builtin containers
    dict, list, tuple, and set.

    ChainMap     - dict-like class for creating a single view of multiple mappings
    Counter      - dict subclass for counting hashable objects
    deque        - list-like container with fast appends and pops on either end
    OrderedDict  - dict subclass that remembers the order entries were added
    defaultDict  - dict subclass that call a factory function to supply missing values
    namedtuple() - factory function for creating tuple subclasses with named fields
    UserDict     - wrapper around dictionary objects for easier dict subclassing
    UserList     - wrapper around list objects for easier list subclassing
    UserString   - wrapper around string objects for easier string subclassing

"""
from collections import ChainMap, Counter, deque, defaultdict, OrderedDict, namedtuple


def _chainmap(*args):
    """ collections module chainmap usecase """
    maps = ChainMap(*args)

    return dict(maps)


def _normalmap(*args):
    """ using dictionary update method """
    maps = {}

    for d in args:
        maps.update(d)

    return dict(maps)


def _counter(hashable_object):
    """ count hashable objects using counter objects
        - can easily append items to left or right end
        - can delete items from left or right end
        - can extend iterable to the left or right end
        - can rotate elements n position to left or right
    """
    counter = Counter(hashable_object)
    return dict(counter)


def _deque(name):
    """  deque object creation and manipulation """
    qued = deque(name)

    qued.appendleft("!Fifa ")
    qued.append(" 2020 !")

    qued.popleft()
    qued.pop()

    qued.rotate(4)
    return tuple(qued)


def _ordered_dict(maps):
    """ implementing ordereddict usecase """

    d = OrderedDict(maps)

    print(d)
    d.move_to_end('a')
    print(d)

    d.popitem(last=True)
    print(d)

    d.popitem(last=True)
    print(d)


def _default_dict(s):
    """ implementing defaultdict usecase """

    # default values as list
    default = defaultdict(list)

    # default value as NotFound, ensures that if key is not found in dict puts its value as NotFound
    defaults = defaultdict(lambda: "NotFound")
    defaults['a'] = 97
    defaults['a'] = 97
    print(defaults['c'])     # gives NotFound instead or keyErro

    for k, v in s:
        default[k] = v

    return default


def _namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, y=22)     # instantiate with positional or keyword arguments
    p[0] + p[1]             # indexable like the plain tuple (11, 22)
    x, y = p                # unpack like a regular tuple
    print(x, y)
    print(p.x + p.y)        # fields also accessible by name

    l = [3, 4]
    named = Point._make(l)
    print(named._asdict())
    print(named._replace(x=33, y=44))
    print(named._fields)


def main():
    """ entrypoint for program execution """
    map0 = {'a': 1, 'b': 2, 'c': 3}
    map1 = {'A': 1, 'B': 2, 'C': 3}
    map2 = {'i': 1, 'ii': 2, 'iii': 3}
    count_list = [1, 2, 3, 4, 1, 3, 4, 5, 6, 7, 2, 3, 5, 7, 8, 1, 9, 0]
    name = 'worldcup'
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

    """ uncomment to test """
    # update 3 maps into single map object
    # maps = _chainmap(map0, map1, map2)
    # print(maps)

    # maps = _chainmap(map0, map1, map2)
    # print(maps)

    # count no of repetated items in list
    # counter = _counter(count_list)
    # print(counter)

    # convert list to deque object and perform opertations
    # qued = _deque(name)
    # print(qued)

    # using list as the default_factory
    # s = _default_dict(s)
    # print(s)

    # _ordered_dict(map0)
    # _namedtuple()


if __name__ == "__main__":
    main()
