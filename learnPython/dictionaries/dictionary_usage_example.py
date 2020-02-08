
def dictionary_usage_example():
    func_name = "dictionary_usage_example - "
    print(func_name + "start")
    dictionary_definition_example()
    print(func_name + "end")


def dictionary_definition_example():
    func_name = "dictionary_definition_example - "
    print(func_name + "start")
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Notes:
    # 0) The keys in a dictionary have to be hashable.
    # Integers, floating point numbers, strings, tuples, and frozensets are hashable, while lists,
    # dictionaries, and sets other than frozensets are not.
    # 1) The values of a dictionary does NOT have to be ALL of the same types.
    # 2) The keys of a given dictionary does NOT have to ALL of the same types.

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    my_dict1 = {"key1": "val1", "key2": 2}
    print(func_name + "my_dict1 is:" + str(my_dict1))

    # 2)
    my_dict2 = {"key1": 1, 44: "val2"}
    print(func_name + "my_dict2 is:" + str(my_dict2))

    print(func_name + "end")