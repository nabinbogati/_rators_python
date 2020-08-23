"""
    Generator are special type of function which does not return single value,
    instead returns an iterator object with a sequence of values.
    In a generator a yield statement is used instead of return statement.
    Basically, a generator provides a way to create our own iterator.
"""

def my_generator():
    print('First Item')
    yield 10

    print('Second Item')
    yield 20

    print('Third Item')
    yield 30


def loop_generator():
    for i in range(10):
        yield i


"""
    yield - pauses the execution
    next - resumes the execution
    terminates on encountering StopIteration Error

    keep in mind that yield returns a value and pauses the execution of the function while maintaning
    the internal states, whereas return simply returns the value and terminates the execution of the function.
"""


def gen_expression():
    """
        demonstrates a generator expression, a shorter way of defining a simple generator function.
        Generator Expression is an anonymous generator
    """

    my_generator_exp = (x*x for x in range(5))

    print(next(my_generator_exp))
    print(next(my_generator_exp))
    print(next(my_generator_exp))
    print(next(my_generator_exp))

if __name__ == '__main__':
    gen = my_generator()
    
    # properly calling a generator function
    loop = loop_generator()

    while True:
        try:
            print("Loop on next: ", next(loop))
        except StopIteration:
            break

    # using loop to traversing over the iterator object return by generator,
    # next function is called implicitly and StopIteration is taken care
    for gene in gen:
        print(gene)


    gen_expression()
    # in this case the generator object is empt
    next(gen)
    next(gen)
    next(gen)
    next(gen)

    # in this case the generator object is empt
    next(loop)
    next(loop)
    next(loop)
    next(loop)

