#########################################################################################
#########################################################################################
# Good link that illustrate the name and namespace concept:
# https://www.programiz.com/python-programming/namespace
#
# Name and namespaces in Python:
# ------------------------------
# 1) A name (also called identifier) is simply a name given to objects.
# Everything in Python is an object. Name is a way to access the underlying
# object.
# 2) When Python "defines" an object with a value they both (initialy) "points"
# to the same address in memory.
# 3) The new value (18 in this case) that int_obj now refers to, gets a "new"
# address in memory. If the address of the object 18 should be displayed it will
# point to this same place as well.
# 4) Furthermore, when we do int_obj2 = int_obj_initial_val, the new name int_obj2
# gets associated with the previous object which is 17 in this case.
# This is efficient as Python doesn't have to create a new duplicate object.
# This dynamic nature of name binding makes Python powerful; a name could refer to any
# type of object.
#
#########################################################################################
#########################################################################################
from learnPython.chapter_9_objects.otherModule import other_module_outer_func
from learnPython.chapter_9_objects.otherModuleGlobalVar import other_module_outer_func_global


def name_illustration():
    func_name = "name_illustration - "
    print(func_name + "start")
    int_obj_initial_val = 17
    print(func_name + "initializing an int_obj with initial value of:" + str(int_obj_initial_val))
    # 1)
    int_obj = 17
    print(func_name + "id(int_obj):" + str(id(int_obj)))
    # 2)
    print(func_name + "the address (in RAM) of the value is:" + str(id(17)))
    # 3)
    int_obj += 1 # it is now set to 18
    print(func_name + "after incrementing the value of int_obj by one it's new"
          + " value is:" + str(int_obj) + ", and its address is:" + str(id(int_obj))
          + " and the address is id(18):" + str(id(18)))
    # 4)
    int_obj2 = int_obj_initial_val
    print(func_name + "the int_obj2 was set to int_obj_initial_val, thus it points to:"
          + str(id(int_obj2)))
    print(func_name + "still, the address of it's initial value is:" + str(id(int_obj_initial_val)))
    print(func_name + "end")


def namespace_illustration_in_other_module():
    func_name = "namespace_illustration_in_other_module - "
    print(func_name + "start")
    other_module_outer_func()
    other_module_outer_func_global()
    print(func_name + "end")


def namespace_example():
    func_name = "namespace_example - "
    print(func_name + "start")
    name_illustration()
    print("\n \n \n")
    namespace_illustration_in_other_module()
    print(func_name + "end")

# GLOBAL namespace
x = 12

def func1():
    # ENCLOSING namespace
    x = 15
    
    def func2():
        # LOCAL namespace
        x = 17
        print("func2 - x is:" + str(x))

    def func3():
        # When using the global keyword - the variable that is taking into
        # account is NOT the "next outer" but the actual GLOBAL vartiable - i.e. the vartiable
        # that is defined outside of ANY function within this module (Python file in this case)
	# so in this case, the statment below will print 12 (global value)
        global x 
        print("func3 - x is:" + str(x))
        
    func2()
    func3()

print("about to call func1")
func1()

if __name__ == "__main__":
	namespace_example()
