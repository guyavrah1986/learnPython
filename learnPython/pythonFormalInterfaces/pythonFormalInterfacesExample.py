#########################################################################################################
#########################################################################################################
# Python formal interface:
# ------------------------
# In a way, they are very similar to C++ classes where all the methods are pure virtual functions (i.e. 
# pure virtual class), thus inheriting from this class enforces the sub classes to implement all the 
# functions of the interface's class.
# 1) Creating a Male object is possible cause it implemnts all the interface's methods.
# 2) Creating a Female object is NOT possible cause it does NOT implement all the interface's method.
#########################################################################################################
#########################################################################################################
import abc


class PersonInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "get_name") and
                callable(subclass.load_data_source) and
                hasattr(subclass, "get_age") and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_age(self):
        raise NotImplementedError


class Male(PersonInterface):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Female(PersonInterface):

    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


def python_formal_interface_example():
    func_name = "python_formal_interface_example - "
    print(func_name + "start")
    print(func_name + "about to create a Male object")
    # 1)
    male_obj = Male("Rotem", 33)

    # 2)
    #print(func_name + "about to create Female object")
    #female_obj = Female("Roni")
    print(func_name + "end")


if __name__ == "__main__":
    python_formal_interface_example()
