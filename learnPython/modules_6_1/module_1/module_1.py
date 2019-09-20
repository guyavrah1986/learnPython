import inspect

from learnPython.utilities.loggable import Loggable
from learnPython.modules_6_1.module_2.module_2 import func1


def modules_usage_examples():
    func_name = inspect.stack()[0][3] + " - "
    print(func_name + "start")
    arg1 = 17
    print(func_name + "about to call func1 of module_2")
    func1(arg1)



class Module1Class(Loggable):

    def __init__(self):
        Loggable.__init__(self, self.m_class_name)
        print(self.log_me())

    def modules_usage_examples(self):
        print(self.log_me + "start")