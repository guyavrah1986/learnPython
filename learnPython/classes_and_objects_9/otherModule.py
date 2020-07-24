#########################################################################################
#########################################################################################
# 1) The variable a here is in the global namespace - it is "known" throughout this
# entire module (essentially Python file).
#
#########################################################################################
#########################################################################################


def other_module_outer_func():
    func_name = "other_module_outer_func - "
    a = 20

    def other_module_inner_func():
        func_name = "other_module_inner_func - "
        a = 30
        print(func_name + "a is:" + str(a))

    other_module_inner_func()
    print(func_name + "a is:" + str(a))


# 1)
a = 10
print(__name__ + " - a is:" + str(a))
