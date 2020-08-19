"""
 functions in python are first class objects. Hence, we can pass function as an argument and return functions too.
 So, decorators are those functions which accepts function as an argument and returns fuctions as  output of function.
 Decorators can be used in adding functionalities to underlying functions or user_defined functions without actually modifiying original function.
"""


def decor(func):
    def wrapper(*args):
        print("Your Name Is: ")
        func(*args)
        
    return wrapper


@decor
def print_name(name):
    print(name)



if __name__ == '__main__':
    result_func = decor(print_name)
    result_func("nb")

    """
        Additionally, we can use python handy decorator feature @decorator_name to implictly call the decorator function 
    """
    print_name("nb")

