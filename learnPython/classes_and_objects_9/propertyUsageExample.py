
class Family:

    def __init__(self, family_name):
        self.__family_name = family_name

    @property
    def name(self):
        return self.__family_name


class Child(Family):

    def __init__(self, family_name, child_name):
        super(Child, self).__init__(family_name)
        self.__child_name = child_name

    @property
    def name(self):
        return (self.__child_name, super(Child, self).name)


def property_usage_example_in_derived_class():
    func_name = "property_usage_example_in_derived_class - "
    print(func_name + "start")
    child_obj = Child("Elbaz", "Yonatan")
    print(func_name + "the child_obj full name is:" + " ".join(child_obj.name))
    print(func_name + "end")


if __name__ == "__main__":
    property_usage_example_in_derived_class()