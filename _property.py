"""
    In object orient programming aproach, each class has getter, setter and delter methods. Those methods are handy tool to maintain eccapsulation throught the class and providing access to private fields and methods.
    In python3 private fields, methods can be defined as:
        fields/methods starting with _ are refered as protected
        fields/methods starting with __ are refered as private

    Hence, getter, setter and deleter methods are used to access those fields and variables.

    To make those methods accessable easily python provides built in property feature with decorator. It accepts (getter, setter, deleter, doc) as an argument and return corresponding values.

"""


class person:
    def __init__(self, name="Guest"):
        self.__name=name

    def setname(self, name):
        self.__name=name

    def getname(self):
        return self.__name

    def delname(self):
        del self.__name

    # setting property function to a variable
    prop = property(getname, setname, delname)


# using property feature as a decorator
class persons:
    def __init__(self):
        self.__name = ''

    @property # decorate getter method with builtin special decorator
    def name(self):
        return self.__name

    @name.setter # define to decorator its a setter method
    def name(self, value):
        self.__name = value

    @name.deleter # define to decorator its a deleter method
    def name(self):
        print('Deleting..')
        del self.__name


if __name__ == '__main__':
    p = persons()
    p.name = "nb"
    print(p.name)
    del p.name


    # flow with property function
    p2 = person()
    p2.prop = "nb"
    print(p2.prop)

    # flow without property function
    p = person()
    p.getname()
    p.setname("nb")
    p.getname()
