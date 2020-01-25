
def other_module_outer_func_global():
    func_name = "other_module_outer_func_global - "
    global b
    b = 20

    def other_module_inner_func():
        func_name = "other_module_inner_func - "
        global b
        b = 30
        print(func_name + "b is:" + str(b))

    other_module_inner_func()
    print(func_name + "b is:" + str(b))


b = 10
print(__name__ + " - b is:" + str(b))
