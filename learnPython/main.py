import sys

from learnPython.strings_3_1_2.stringsUsageExample import strings_usage_example
from learnPython.templateMethodPattern.templateMethodPattern import template_method_pattern_usage_example
from learnPython.lists_3_1_3.listsUsageExample import lists_usage_example
from learnPython.functions_4_7.functionDefinitionAndExecutionUsageExample import functions_definition_and_execution_usage_example
from learnPython.tcpdumpRunner.tcpdumpRunner import run_tcpdump_on_local_machine
from learnPython.threading_11_4.threadingUsageExample import threading_usage_example
from learnPython.scapyExample.scapyExample import scapy_usage_example


def call_proper_usage_function(argv):
    func_name = "call_proper_usage_function - "
    print(func_name + "got arguments:\n")
    print(argv)
    if argv[1] == "stringUsage":
        strings_usage_example()
    elif argv[1] == "templateMethodPattern":
        template_method_pattern_usage_example()
    elif argv[1] == "listsUsage":
        lists_usage_example()
    elif argv[1] == "functionsUsage":
        functions_definition_and_execution_usage_example()
    elif argv[1] == "runTcpdump":
        run_tcpdump_on_local_machine()
    elif argv[1] == "runThreadingUsageExample":
        threading_usage_example()
    elif argv[1] == "scapyUsageExample":
        scapy_usage_example(argv[2:])
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


if __name__ == "__main__":
    main(sys.argv)