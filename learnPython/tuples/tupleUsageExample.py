

def tuple_usage_example():
    func_name = "tuple_usage_example - "
    print(func_name + "start")
    print(func_name + "end")
    my_tuple = ("1", "a", "b", "5", "a")
    print(func_name + "my_tuple is:" + str(my_tuple))
    val_to_look = "a"
    num_of_appearances = my_tuple.count(val_to_look)
    print(func_name + "the number of appearances of the value:" + val_to_look + " is " + str(val_to_look))
    if num_of_appearances > 1:
        print(func_name + "the first appearances of " + val_to_look + " is at index:" + str(my_tuple.index(val_to_look)))

    print(func_name + "end")