from learnPython.functions_4_7.sampleObject import SampleObject


def functions_definition_and_execution_usage_example():
    func_name = "functions_definition_and_execution_usage_example - "
    print(func_name + "start")
    dict_as_arg_to_func = {"key1": "val1", "key2": 89, "key3": [12, 15, 17]}
    func_with_kwargs(key1="val1", key2=2, key3=[12, 15, 17])
    func_with_arbitrary_number_of_arguments(1, 2, "Rotem", 7.8)
    function_call_example()
    passing_object_to_func()
    passing_object_to_func()
    print(func_name + "end")


def func_with_kwargs(**kwargs):
    """
    Functions that have the **kwargs as their argument actually receive from the user a dictionary of the form:
    {arg1_name:arg1_val, arg2_name:arg2_val, ...}. 
    """
    key_in_dict_args = "some_key"
    if key_in_dict_args in kwargs:
        print("the value of the key:" + key_in_dict_args + ", is:" + str(kwargs[key_in_dict_args]))
    else:
        print("the key:" + key_in_dict_args + " is NOT in the received dictionary")
    print("got the following dictionary as argument:")
    for key, val in kwargs.items():
        print(str(key) + "," + str(val))


def func_with_arbitrary_number_of_arguments(*args):
    """
    Functions with a single argument noted by * can receive as many arguments as needed, where the only thing to note here is that
    all the arguments that are passed are treated (in the function) as a tuple. So if the function is called as follows:
    func_with_arbitrary_number_of_arguments(1,2,3) --> then the arguments sent to the function are the following tuple: (1, 2, 3)
    """
    func_name = "func_with_arbitrary_number_of_arguments - "
    print(func_name + "start")
    arg_num = 0
    for arg in args:
        print(func_name + "arg[" + str(arg_num) + "]:" + str(arg))


def function_call_example():
    func_name = "function_call_example - "
    print(func_name + "start")
    # this example illustrate that the passing arguments mechanism in Python is "call
    # by value" - the integer and the string objects that were defined in the caller function
    # and were sent and modified in the callee function, did NOT change in the caller function.
    caller_func()
    print(func_name + "end")


def caller_func() -> None:
    """
    Note that both str (string in Python) and int (integer in Python) are IMMUTABLE object, so when one pass
    them to some function, their original value does NOT change in the caller function.
    :return: None
    """
    func_name = "caller_func - "
    var1_func1 = "var1_func1"
    var2_func1 = 17
    x = 12
    print(func_name + "var1_func1:" + var1_func1 + ", var2_fun1:" + str(var2_func1), ", x:" + str(x))
    calle_func(var1_func1, x)
    print(func_name + "back from calle_func, var1_func1:" + str(var1_func1) + ", x is:" + str(x))


def calle_func(arg1: str, x: int) -> None:
    func_name = "calle_func - "
    print(func_name + "got arg1:" + arg1 + ", x:" + str(x))
    arg1 = "var1_func2"
    x = 15
    print(func_name + "set arg1 to:" + arg1 + ", x to:" + str(x))


def passing_object_to_func():
    func_name = "passing_object_to_func - "
    print(func_name + "about to create SampleObject")
    sample_obj = SampleObject(17)
    print(func_name + "before calling callee_func, sample_obj.num is:" + str(sample_obj.num))
    ret_val = callee_func(sample_obj)
    if ret_val:
        print(func_name + "callee_func was NOT successful")
    else:
        print(func_name + "after calling callee_func, sample_obj.num is:" + str(sample_obj.num))

    print(func_name + "about to call set_arg_obj_to_none(sample_obj)")
    sample_obj = set_arg_obj_to_none(sample_obj)
    if sample_obj is None:
        print(func_name + "after calling set_arg_obj_to_none(sample_obj), sample_obj is indeed None")
    else:
        print(func_name + "after calling set_arg_obj_to_none(sample_obj), sample_obj is NOT None")


def callee_func(sample_object):
    func_name = "callee_func - "
    if sample_object is None:
        print(func_name + "got a None object")
        return False

    if type(sample_object) is SampleObject:
        print(func_name + "got a SampleObject")
        sample_object.func1()
    else:
        print(func_name + "got an object that is NOT of type SampleObject")
        return False

    return True


def set_arg_obj_to_none(sample_obj):
    func_name = "set_arg_obj_to_none - "
    print(func_name + "setting the received object to None")
    sample_obj = None
    return sample_obj


def func_with_immutable_default_argument(num, def_list=[]):
    def_list.append(num)
    return def_list


def call_func_with_immutable_default_argument_several_times():
    func_name = "call_func_with_immutable_default_argument_several_times - "
    call_number = 1
    print(func_name + "after call number:" + str(call_number) + func_with_immutable_default_argument(1))
    call_number += 1
    print(func_name + "after call number:" + str(call_number) + func_with_immutable_default_argument(2))
    call_number += 1
    print(func_name + "after call number:" + str(call_number) + func_with_immutable_default_argument(3))


if __name__ == "__main__":
    functions_definition_and_execution_usage_example()