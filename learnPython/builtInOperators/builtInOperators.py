

def built_in_operators_usage_example():
    func_name = "built_in_operators_usage_example - "
    print(func_name + "start")

    # the enumerate built in operator "encapsulates" the items in an iterable object (string, list,etc...)
    # to a tuple composed of: value,index
    # list into a tuple
    my_string = "abcd"
    print(func_name + "enumerating " + my_string + "returns:")
    for item1, item2 in enumerate(my_string):
        print(item1, item2)

    my_list1 = [1, 2, 3]
    my_list2 = ["a", "b", "c"]
    # the zip operator zips two items in the same index in the list provided and create a tuple out of them
    print(func_name + "after zipping " + str(my_list1) + " and " + str(my_list2) + " the tuples are:")
    for item in zip(my_list1, my_list2):
        print(item)

    # a pythonic way to compose list can be done with list comprehensions
    my_new_list = [letter for letter in "abcde"]
    print(func_name + "my_new_list is:" + str(my_new_list))
    print(func_name + "end")
    
def my_square_func(num: int) -> int:
    return num * num

def map_example():
    func_name = "map_example - "
    print(func_name + "start")
    num_list = [1, 2, 3]
    index = 0
    for item in map(my_square_func, num_list):
        print(func_name + "the square value of:" + str(num_list[index]) + " is:" + str(item))
        index += 1
    print(func_name + "end")
