
def exception_handling_usage_example():
    func_name = "exception_handling_usage_example - "
    print(func_name + "start")
    func_that_raise_exception()
    func_that_catches_multiple_exception_types()
    print(func_name + "end")


def func_that_raise_exception():
    func_name = "func_that_raise_exception - "
    print(func_name + "start")
    try:
        print(func_name + "start of the try block")
        raise TypeError
    except TypeError as e:
        print(func_name + "caught a TypeError exception:" + str(e))
    finally:
        print(func_name + "within the finally block - this block runs whether or not there was an error")

    print(func_name + "end")


def func_that_catches_multiple_exception_types():
    func_name = "func_that_catches_multiple_exception_types - "
    print(func_name + "start")
    try:
        raise KeyError
    except TypeError as e:
        print(func_name + "caught a " + e.__class__.__name__ + " exception")
    except KeyError as e:
        print(func_name + "caught a " + e.__class__.__name__ + " exception")
    except:
        print(func_name + "caught a general exception")

    print(func_name + "end")


if __name__ == "__main__":
    exception_handling_usage_example()
