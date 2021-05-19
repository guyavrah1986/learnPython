
def lists_usage_example():
    func_name = "lists_usage_example - "
    print(func_name + "start")
    basic_usage_lists()
    print(func_name + "end")


def basic_usage_lists():
    func_name = "basic_usage_lists - "
    print(func_name + "start")
    list1 = [1, 2, 3, 4]
    print(func_name + "list1:" + str(list1))
    # unlike strings (for example) which is an IMMUTABLE object, lists CAN be
    # changed (they are MUTABLE):
    list1[1] = 0
    print(func_name + "after setting the second element, list1:" + str(list1))
    list2 = [5, 6, 7, 8]
    # list concatenation is also possible
    list3 = list1 + list2
    print(func_name + "list3(list1 + list2):" + str(list3))
    # it is possible to define list of lists
    list4 = [list1, list3]
    # list can hold values of different types
    diff_types_list = [True, 12, "string", 17.15]
    print(func_name + "the list with the different types of values is:\n" + str(diff_types_list))
    print(func_name + "list4 is:" + str(list4))


if __name__ == "__main__":
    lists_usage_example()