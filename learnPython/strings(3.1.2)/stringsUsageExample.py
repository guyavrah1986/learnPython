
def strings_usage_example():
    func_name = "strings_definition - "
    print(func_name + "start")
    string_definition_example()
    immutablity_of_string()
    print(func_name + "end")


def string_definition_example():
    func_name = "string_definition_example - "
    print(func_name + "start")
    str1 = "Doesn't"
    print(func_name + "str1:" + str1)
    str2 = 'Doesn\'t'
    print(func_name + "str2:" + str2)


def immutablity_of_string():
    func_name = "immutablity_of_string - "
    str1 = "old_str"
    print(func_name + "str1 is:" + str1)
    # if the below line will be commented out, the following error will rise:
    # str1[1] = "b"
    # TypeError: 'str' object does not support item assignment
    # this is because strings are immuatable objects in Python
    #str1[1] = "b"
    #print(func_name + "now str1 is:" + str1)

    # what actually happens here is that a "new string" is being constructed and
    # then aassgined (thus overrides) the old value of str1.
    str1 = "new_str"
    print(func_name + "now str1 is:" + str1)
