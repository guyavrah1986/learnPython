
def functions_definition_and_execution_usage_example():
    func_name = "functions_definition_and_execution_usage_example - "
    print(func_name + "start")
    calle_func()


def caller_func():
    func_name = "caller_func - "
    var1_func1 = "var1_func1"
    var2_func1 = 17
    x = 12
    print(func_name + "var1_func1:" + var1_func1 + ", var2_fun1:" + var2_func1, ", x:" + x)
    calle_func(var1_func1, x)
    print(func_name + "back from calle_func, var1_func1:" + var1_func1 + ", x is:" + x)


def calle_func(arg1, x):
    func_name = "calle_func - "
    print(func_name + "got arg1:" + arg1 + ", x:" + x)
    var2_func1 = 17
    arg1 = "var1_func2"
    x = 15
    print(func_name + "set arg1 to:" + arg1 + ", x to:" + x)