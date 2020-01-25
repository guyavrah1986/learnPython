

class TestObj:

    def __init__(self):
        func_name = "TestObj::__init__ - "
        print(func_name)

    def __test_obj_private_function(self):
        func_name = "TestObj::__test_obj_private_function - "


def example_func():
    func_name = "example_func - "
    print(func_name + "start")

    print(func_name + "end")


if __name__ == "__main__":
	example_func()