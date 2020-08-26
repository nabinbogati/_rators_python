"""
    This value in the enclosing scope is remembered even when the variable goes out of scope
    or the function itself is removed from the current namespace. This property is known as a
    closure property.

    nonlocal keyword is used to accesss the enclosed variables

    It can provide an object oriented solution to the problem.

    This value in the enclosing scope is remembered even when the variable goes out of scope
    or the function itself is removed from the current namespace. This property is known as a
    closure property.

    To have a closure we must have following condition satisfied:
        We must have a nested function (function inside a function).
        The nested function must refer to a value defined in the enclosing function.
        The enclosing function must return the nested function.
    
    can access the value that gets enclosed in closure function vai __closure__ dunder method

"""


def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)


def add1(z=0):
    def add(x, y):
        'add x to y to z'
        nonlocal z
        z += 1
        return x + y + z
    return add


if __name__ == '__main__':
    print_msg(9)
    add = add1(3)
    print(add(2, 4))
