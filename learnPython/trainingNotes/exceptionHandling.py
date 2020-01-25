# The motivation behind exception handling is to be able to "gaurentee" that the
# program will always finish "successfully". Note that it does not mean that it indeed
# performed what it should have done correctly, but nevertheless, it indicated "back" to
# it's "invoker" that it finished without any error (i.e. - its return code is 0).
#
#
# NOTES:
# 1) Whenever catching exceptions, be aware that hte "last" exception type to be caught
# needs to be Python's built-in Exception object. This is crucial due to the fact that
# all other built-in exceptions in Python derives from that object.
# 2) The finally block is used to run whatever block of code that MUST run whether an
# exception was raised or not. A classic example for a scenario like so, is to clode a
# connection to a DB

def func_that_throws_io_error_exception():
    func_name = "func_that_throws_exception - "
    print(func_name + "start")
    #raise Exception("this is my general Exception message")
    raise IOError("this is my IOError Exception message")

    print(func_name + "end")

def func_that_throws_general_exception():
    pass


def main_func():
    func_name = "main_func - "
    print(func_name + "start")
    try:
        func_that_throws_io_error_exception()
    except IOError as e:
        print("caught an IOError:" + str(e))
    except Exception as e:
        print("caught a general exception")
    finally:
        print("finally block start")
        #raise ImportError
        print("finally block end")

    print(func_name + "end")


print("calling the main function")
main_func()