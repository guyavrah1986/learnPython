#################################################################################################################
#################################################################################################################
# 1) MRO - Method Resolution Order:
# The order of methods invocation for classes that inherites from more than a single "base class" is given by
# the MRO "algorithm" which simply put is as follows:
# The methods of all the base classes are searched depth-first and left-to-right.
# --> so in this case when calling the derived_obj.func3(), the "run time search" will first (!!) find that
# func3 is implemented in Base3, so it will invoke it and stop the search.
#
# 2) Same goes for func2 --> it will first find it in Base2 (after looking in Base3 and NOT finding it), thus
# this will be the invoked function and the search will terminate. 
#################################################################################################################
#################################################################################################################


class Base1:

    def __init__(self, b1):
        self.b1 = b1
        print(__class__.__name__ + "::" + "__init__" + "self.b1 is:" + str(self.b1))

    def func1(self):
        func_name = "func1 - "
        print(__class__.__name__ + "::" + func_name + "self.b1 is:" + str(self.b1))

    def func2(self):
        func_name = "func2 - "
        print(__class__.__name__ + "::" + func_name)

    def func3(self):
        func_name = "func3 - "
        print(__class__.__name__ + "::" + func_name)


class Base2(Base1):

    def __init__(self, b2):
        self.b2 = b2
        print(__class__.__name__ + "::" + "__init__" + "self.b2 is:" + str(self.b2))

    def func2(self):
        func_name = "func2 - "
        print(__class__.__name__ + "::" + func_name + "self.b2 is:" + str(self.b2))


class Base3(Base1):

    def __init__(self, b3):
        self.b3 = b3
        print(__class__.__name__ + "::" + "__init__" + "self.b3 is:" + str(self.b3))

    def func3(self):
        func_name = "func3 - "
        print(__class__.__name__ + "::" + func_name + "self.b3 is:" + str(self.b3))


class Derived(Base3, Base2, Base1):

    def __init__(self, b3, b2, b1):
        Base3.__init__(self, b3)
        Base2.__init__(self, b2)
        Base1.__init__(self, b1)
        print(__class__.__name__ + "::" + "__init__")


def multiple_inheritance_example():
    func_name = "multiple_inheritance_example - "
    print(func_name + "start")
    print(func_name + "creating a Derived class (that derived from 3 Base classes)")
    derived_obj = Derived(3,2,1)
    print(func_name + "Derived object MRO is:" + str(Derived.mro()))
    print(func_name + "calling derived_obj.func1()")
    derived_obj.func1()
    print(func_name + "calling derived_obj.func3()")
    derived_obj.func3()  # 1)
    print(func_name + "calling derived_obj.func2()")
    derived_obj.func2()  # 2)
    print(func_name + "end")


if __name__ == "__main__":
    multiple_inheritance_example()