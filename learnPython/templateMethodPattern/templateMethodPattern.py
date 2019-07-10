
def template_method_pattern_usage_example():
    func_name = "template_method_pattern_usage_example - "
    print(func_name + "creating Base object and calling its method")
    base_obj = Base()
    base_obj.method1()
    print("\n \n")
    print(func_name + "creating Derived object and calling its method")
    derived_obj = Derived()
    derived_obj.method1()


class Base:

    def __init__(self):
        self.base_val = 1
        print("Base::__init__")

    def method1(self):
        print("Base::method1")
        self._my_specific_method1_extension()
        print("Base::method1 - base_val is:" + str(self.base_val))
        print("Base::method1 - end")

    def _my_specific_method1_extension(self):
        print("Base::_my_specific_method1_extension")
        self.base_val += 1


class Derived(Base):

    def __init__(self):
        super().__init__()
        print("Derived::__init__")

    def _my_specific_method1_extension(self):
        print("Derived::_my_specific_method1_extension")
        self.base_val += 2