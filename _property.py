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



if __name__ == '__main__':

    # flow with property function
    p2 = person()
    p2.prop = "nb"
    p2.prop

    # flow without property function
    p = person()
    p.getname()
    p.setname("nb")
    p.getname()


