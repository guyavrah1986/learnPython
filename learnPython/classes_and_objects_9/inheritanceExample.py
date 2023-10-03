#########################################################################################
# 1) Every method of a Base class can be overriden by the Derived class. In C++ terms
# every method in the Base class is effectively virtual.
#
# 2) It is possible to "enforce" invocation" of a method of the Base class by explicitly
# use the notation BaseClassName.base_class_method(self, arguments)
#
#########################################################################################


class BaseClass:

    def __init__(self, b):
        self.b = b

    def func1(self):
        func_name = "func1 - "
        print(__class__.__name__ + "::" + func_name + "self.b is:" + str(self.b))

    def func2(self):
        func_name = "func2 - "
        print(__class__.__name__ + "::" + func_name)


class DerivedClass(BaseClass):

    def __init__(self, b):
        BaseClass.__init__(self, b)

    def func1(self):
        # 1)
        func_name = "func1 - "
        print(__class__.__name__ + "::" + func_name + "self.b is:" + str(self.b))

    def func2(self):
        # 2)
        BaseClass.func2(self)


def simple_inheritance_example():
    func_name = "simple_inheritance_example - "
    print(func_name + "start")
    print(func_name + "creating a Dervied object")
    derived_obj = DerivedClass(17)
    print(func_name + "calling derived_obj.func1()")
    derived_obj.func1()
    print(func_name + "calling derived_obj.func2()")
    derived_obj.func2()

    print(func_name + "end")


if __name__ == "__main__":
    simple_inheritance_example()
