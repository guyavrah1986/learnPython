

class SampleObject(object):

    def __init__(self, num):
        func_name = "__init__ - "
        self.num = num
        print(func_name)

    def func1(self):
        func_name = "func1 - "
        self.num += 1
        print(func_name + "self.num is:" + str(self.num))