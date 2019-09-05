import inspect

from learnPython.utilities.loggable import Loggable


def modules_usage_examples():
    func_name = print(inspect.stack()[0][3]) + " - "
    print()


class Module1Class(Loggable):

    def __init__(self):
        Loggable.__init__(self, self.m_class_name)
        print(self.log_me())

    def modules_usage_examples(self):
        print(self.log_me + "start")