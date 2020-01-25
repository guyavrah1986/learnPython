
class MyDerivedClass(MyClass):

    def __init__(self, num):
        super().__init__(num)

    def print_protected_class_member(self):
        print("MyDerivedClass::print_protected_class_member - the protected class member"
              + " value is:" + str(self._protected_member))



class MyInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def func_1_interface(self, num):
        """
        pass
        :param num:
        :type num:
        :return:
        :rtype:
        """
        pass

    @abc.abstractmethod
    def func_2_interface(self, str, age):
        pass


class MyImplementedClass(MyInterface):

    def __init__(self):
        print("MyImplementedClass::__init__")

    def some_func(self):
        print("MyImplementedClass::some_func")

#print("trying to create an instance of MyImplementedClass")
#my_implemented_class_instance = MyImplementedClass()