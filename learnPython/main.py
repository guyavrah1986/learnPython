import sys

from learnPython.strings.stringsUsageExample import strings_usage_example


def call_proper_usage_function(*argv):
    func_name = "call_proper_usage_function - "
    print(func_name+ "got arguments:\n")
    print(argv)
    if argv[1] == "stringUsage":
        strings_usage_example()
    else:
        print(func_name + "got an invalid argument")

    print(func_name + "end")

def main(argv):
    func_name = "main - "
    print(func_name + "start")
    print(func_name + "got command line arguments:\n")
    print(argv)
    call_proper_usage_function(argv)
    print(func_name + "end")


if __name__== "__main__":
    main(sys.argv)