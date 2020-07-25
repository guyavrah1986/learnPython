###########################################################################################################
# Pass by assignment:
# In contrast to other programming languages, such as Java/C++, in Python there is NO really pass by
# reference mechanism. Here it is called (and performed) as pass by assignment.
# 1) If the object type that is being passed is IMMUTABLE:
# 1.1) It can NOT be altered by the function, meaning any "reassignment" that takes place in the function
# on the "function's argument" is relevant to this argument and NOT to the original variable (object) that
# was sent to the function. This is due to the fact that a "copy" of the reference to the object is what
# being sent to the function.
# IMMUTABLE object in Python are:
# - string (str)
# - tuple
# - primitive types: int, bool, decimal, float,
# -range
# 2) If the object type being passed is MUTABLE:
# 2.1) It can be altered by the function, meaning, changing "part" of it (for example, an item in a list)
# is possible, meaning, when passing a mutable object to a function, each change in the content of the
# object itself, is reflected in the "original" object from the calling function.
# 2.2) When passing a MUTABLE object to a function and it is being reassigned within it, the original
# object from the calling function will NOT be altered.
###########################################################################################################


def change_string_content(string: str):
    func_name = "change_string_content - "
    print(func_name + "got string:" + string)
    string += "_with_function_addition"
    print(func_name + "after modifying the string in the function it is:" + string)


def change_list_content(list_to_change: list):
    func_name = "change_list_content - "
    print(func_name + "the list that is received with id:" + str(id(list_to_change)) + " has initially the"
          + " content:" + str(list_to_change))
    list_to_change.append(4)


def change_list_assignment(list_to_change: list):
    func_name = "change_list_assignment - "
    print(func_name + "the list that was received had id:" + str(id(list_to_change)) + " and its content:"
          + str(list_to_change))
    list_to_change = [1, 2, 3, 4, 5]


def pass_mutable_object_to_func():
    func_name = "pass_mutable_object_to_func - "
    print(func_name + "start")
    orig_list = [1, 2, 3]
    print(func_name + "BEFORE passing the orig_list id is:" + str(id(orig_list)) + " and its content is:"
          + str(orig_list))
    change_list_content(orig_list)
    print(func_name + "AFTER passing the orig_list, its content is:" + str(orig_list))
    change_list_assignment(orig_list)
    print(func_name + "AFTER passing again the orig_list, its content is:" + str(orig_list))
    print(func_name + "end")


def pass_immutable_object_to_func():
    func_name = "pass_immutable_object_to_func - "
    print(func_name + "start")
    orig_str = "orig_str"
    print(func_name + "BEFORE passing the original string to the function is it:" + orig_str)
    # 1)
    change_string_content(orig_str)
    print(func_name + "AFTER passing the original string to the function is it:" + orig_str)
    print(func_name + "end")


if __name__ == "__main__":
    pass_mutable_object_to_func()
    pass_immutable_object_to_func()