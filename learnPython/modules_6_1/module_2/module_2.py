
# This is a "module's global" variable
global_var_1 = __name__ + " global variable"


# this is a modules' "public" function. Once you import this module (file) within another module
# - this function can be used
def func1(arg1):
    func_name = __name__ + "::func1 - "
    print(func_name + "start")
    print(func_name + "got arg:" + str(arg1))
    print(func_name + "end")


print("this is a \"stand alone\" statement within " + __name__ + " module")