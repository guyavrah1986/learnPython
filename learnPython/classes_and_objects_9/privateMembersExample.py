#########################################################################################
#########################################################################################
# 1) In Python, there is no really "private" access specifier for class methods/members.
# The convention, yet, is that a class attribute (method/member) that starts with double
# underscores, i.e. - for instance: self.__class_member, is considered to be implementation
# detail and should NOT be accessed by the "client" of the class.
# 2) What really going on under the hood is name mangling. When a class attribute (class member
# or method) with double underscores is met, it is simply "replaced" with the following
# textual replacement:
# obj_instance = ClassName()
# obj_instance._ClassName__private_class_member
# --> so if "manually" one performs this "textual replacement" then it CAN access a private
# class member (for instance).
# 3) Trying to "straight forward" access some "protected" or "private" class method/member
# will NOT work.
# Private members/method (double leading underscore) are going over name mangling "procedure"
# under the hood (mainly to avoid name clashes in derived classes).
#
#########################################################################################
#########################################################################################


class BaseClass(object):

    def __init__(self, p1, p2):
        self.public_member = p1
        self.__private_member = p2

    def _boo(self):
        func_name = "_boo"
        return func_name

    def __foo(self):
        func_name = "__foo"
        return func_name


class DerivedClass(BaseClass):

    def __init__(self, p1, p2, derived_class_member_val):
        BaseClass.__init__(self, p1, p2)
        self.derived_class_member = derived_class_member_val

    def calling_protected_method_of_parent_class(self):
        return self._boo()


def private_class_members_example():
    func_name = "private_class_members_example - "
    print(func_name + "start")
    base_class_obj = BaseClass(15, 17)
    print(func_name + "base_class_obj.public_member is:" + str(base_class_obj.public_member))
    print(func_name + "the BaseClass attributes are:" + str(BaseClass.__dict__.keys()))
    print(func_name + 'calling the "private" method of BaseClass is:' + base_class_obj._BaseClass__foo())
    print(func_name + "base_class_obj.__private_member is:" + str(base_class_obj._BaseClass__private_member))
    # 3)
    #print(func_name + "trying to directly access the private member:" + str(base_class_obj.__private_member))
    #print(func_name + "base_class_obj.__foo() returns:" + base_class_obj.__foo())
    print(func_name + "base_class_obj._boo() returns:" + base_class_obj._boo())
    print(func_name + "end")

def protected_class_method_example():
    func_name = "protected_class_method_example - "
    print(func_name + "start")
    print(func_name + "Creating a DerivedClass")
    derived_class_obj = DerivedClass(2, 4, 89)
    print(func_name + "invoking the calling_protected_method_of_parent_class of the Derived class returns:" + str(
        derived_class_obj.calling_protected_method_of_parent_class()))

if __name__ == "__main__":
    private_class_members_example()