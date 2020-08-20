"""
    using property feature as a decorator

"""


class person:
    def __init__(self):
        self.__name=''

    @property # decorate getter method with builtin special decorator
    def name(self):
        return self.__name

    @name.setter # define to decorator its a setter method
    def name(self, value):
        self.__name=value

    @name.deleter # define to decorator its a deleter method
    def name(self):
        print('Deleting..')
        del self.__name



if __name__ == '__main__':
    p = person()

    p.name = "nb"
    p.name
    del p.name
