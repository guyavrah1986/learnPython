# magic functions are "Python's way to standardise" usage in "common" capabilities of the
# language. For example, the magic function __str__ is the "Java's ToString()" of
# Python.
# Some general notes:
# 1) All magic function are "private", i.e. - __magicFuncName__
# 2) They have a "predefined" signature (arguments and "expected" return value type,
# such as boolean for example).


class Person:

    def __init__(self, age, name=""):
        self.age = age
        self.name = name

    def __gt__(self, other):
        return self.age > other.age

    def __add__(self, other):
        new_age = self.age + other.age
        p = Person(new_age)
        return p

    def __str__(self):
        str_to_return = "age is:" + str(self.age) + ", and name:" + self.name
        return str_to_return


print("let's compare the age of two Person objects")
p1 = Person(17, "David")
p2 = Person(54, "Baruch")

print("invoking p1 > p2")
if p1 > p2:
    print("p1 > p2")
else:
    print("p2 < p2")


p3 = p1 + p2
print("p3 (which is p1 + p2) age is:" + str(p3.age))


print("\"toString\" of p2 is:" + str(p2))