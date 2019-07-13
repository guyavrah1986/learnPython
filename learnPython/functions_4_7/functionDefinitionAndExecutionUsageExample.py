
def functions_definition_and_execution_usage_example():
    func_name = "functions_definition_and_execution_usage_example - "
    print(func_name + "start")
    function_call_example()
    print(func_name + "end")


def function_call_example():
    func_name = "function_call_example - "
    print(func_name + "start")
    # this example illustrate that the passing arguments mechanism in Python is "call
    # by value" - the integer and the string objects that were defined in the caller function
    # and were sent and modified in the calle function, did NOT change in the caller function.
    caller_func()
    print(func_name + "end")


def caller_func():
    func_name = "caller_func - "
    var1_func1 = "var1_func1"
    var2_func1 = 17
    x = 12
    print(func_name + "var1_func1:" + var1_func1 + ", var2_fun1:" + str(var2_func1), ", x:" + str(x))
    calle_func(var1_func1, x)
    print(func_name + "back from calle_func, var1_func1:" + str(var1_func1) + ", x is:" + str(x))


def calle_func(arg1, x):
    func_name = "calle_func - "
    print(func_name + "got arg1:" + arg1 + ", x:" + str(x))
    arg1 = "var1_func2"
    x = 15
    print(func_name + "set arg1 to:" + arg1 + ", x to:" + str(x))