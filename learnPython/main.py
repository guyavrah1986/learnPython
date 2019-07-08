import sys

from learnPython.strings.stringsUsageExample import strings_definition


def main(argv):
    func_name = "main - "
    print(func_name + "start")
    print(func_name + "got command line arguments:\n")
    print(argv)
    print(func_name + "end")


if __name__== "__main__":
    main(sys.argv)