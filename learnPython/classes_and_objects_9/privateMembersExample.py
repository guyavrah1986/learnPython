#########################################################################################
#########################################################################################
# 1) In Python, there is no really "private" access specifier for class methods/members.
# The convention, yet, is that a class attribute (method/member) that starts with double
# underscores, i.e. - for instance: self.__class_member, is considered to be implemntation
# detail and should NOT be accessed by the "client" of the class.
# 2) What really going on under the hood is name mangling. When a class attribute with
# double underscores is met, it is simply "replaced" with the following textual replacement:
# obj_instance = ClassName()
# obj_instance._ClassName__private_class_member
# --> so if "manually" one performs this "textual replacement" then it CAN access a private
# class member (for instance).
#
#
#########################################################################################
#########################################################################################


class BaseClass(object):

    def __init__(self, p1, p2):
        self.public_member = p1
        self.__private_member = p2

    def __foo(self):
        func_name = "__foo"
        return func_name



def private_class_members_example():
    func_name = "private_class_members_example - "
    print(func_name + "start")
    base_class_obj = BaseClass(15, 17)
    print(func_name + "base_class_obj.public_member is:" + str(base_class_obj.public_member))
    print(func_name + "the BaseClass attributes are:" + str(BaseClass.__dict__.keys()))
    print(func_name + 'calling the "private" method of BaseClass is:' + base_class_obj._BaseClass__foo())
    print(func_name + "base_class_obj.__private_member is:" + str(base_class_obj._BaseClass__private_member))
    print(func_name + "end")


if __name__ == "__main__":
    private_class_members_example()