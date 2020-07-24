#########################################################################################
# 1) When a class definition is entered, a new namespace is created, and used as the
# local scope thus, all assignments to local variables go into this new namespace.
# In particular, function definitions bind the name of the new function here.
#
# 2) It is possible to add a "new" attribute, for instance class member to a particular (!!)
# object instance. Note however, that this "new additional class member" will be relevant
# ONLY for the specific object instance it was added in.
#
# 3) When a function of a class (object) is called, then the "first" argument that is sent
# to it is the actual instance (object) that called it, thus, the following function call:
# my_class_obj.print_me()
# is actually "converted" to the following:
# MyClass.print_me(my_class_obj) --> you got it right, the my_class_obj in run-time is
# the self "first argument".
# The "self" keyword can also be thought of that it serves as an indicator that this function/member
# is NOT static.
#
# 4) All class data members that are defined "in between" the class name and the rest of
# the class's methods are "all instance" member (similar to static class members in C++).
# Instance members are usually (best practice) defined in the class CTOR --> the __init__
# method.
#
# 5) It is also possible to define an instance data member NOT in the CTOR (__init__) method
# BUT it NOT considered as a good practice cause if it is accessed from other class function before
# the class where it is defined, then a run time exception will be thrown.
# It is also worth to mention that when accessing class member, the "inner scope" has advantage
# over the "global" scope.
# 
# upon assignment:
# every variable which is an object is copied by reference
# in any other case (int, float,etc...) is copied by value

# the garbage collector "kicks in" ONLY after there is no references pointed to the
# object (note that it "kicks in" in a non deterministic manner).
#########################################################################################


class MyClass:

    class_data_member = 15

    def __init__(self, num):
        self.num = num
        self.string = ""

    def define_some_class_member(self):
        pass

    def print_me(self):
        # 5)
        self.x = 17
        print("MyClass::print_me - num is:" + str(self.num) + ", string is:" + self.string)
        print("MyClass::print_me - self.x is:" + str(self.x))

    def foo(self):
        print("Hi there form " + __class__.__name__ + "::foo")


def classes_and_object_example():
    func_name = "classes_and_object_example - "
    print(func_name + "creating MyClass object")
    my_class_obj = MyClass(12)
    # 3)
    my_class_obj.print_me()
    foo_method_object = my_class_obj.foo
    print(func_name + "about to call foo method using an object pointing to it")
    foo_method_object()

    print(func_name + "creating MyClass object")
    my_class_obj2 = MyClass(17)
    my_class_obj2.print_me()

    # 2)
    my_class_obj.some_new_instance_member = 90
    print(func_name + "the new additional instance member is:" + str(my_class_obj.some_new_instance_member))
    # print("the new additional instance member is:" + str(my_class_obj2.some_new_instance_member))

    # 4)
    print(func_name + "the \"global\" data member seen by my_class_obj.class_data_member"
          + " is:" + str(my_class_obj.class_data_member))

    print(func_name + "the \"global\" data member seen by my_class_obj2.class_data_member"
          + " is (also):" + str(my_class_obj2.class_data_member))

    # 5)
    my_class_obj2.class_data_member = 99
    print(func_name + "the \"global\" data member seen by my_class_obj2.class_data_member"
          + " after intentionally modifying it is:" + str(my_class_obj2.class_data_member))
    print(func_name + "while on the other hand it is STILL seen by my_class_obj.class_data_member"
          + " as:" + str(my_class_obj.class_data_member))

    # access specifier section
    # ========================
    #my_derived_obj = MyDerivedClass(23)
    #my_derived_obj.print_protected_class_member()

    # when trying to access a private member
    #print("the private member of the object is:" + str(MyClass.__private_member))


if __name__ == "__main__":
    classes_and_object_example()
