
def change_list_content(list_to_change: list):
    func_name = "change_list_content - "
    print(func_name + "the list that is received with id:" + str(id(list_to_change)) + " has initially the"
          + " content:" + str(list_to_change))
    list_to_change.append(4)


def change_list_assignment(list_to_change: list):
    func_namme = "change_list_assignment - "
    print(func_namme + "the list that was received had id:" + str(id(list_to_change)) + " and its content:"
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


if __name__ == "__main__":
    pass_mutable_object_to_func()