# the motivation to implement an iterator for a custom class is that if, for example,
# this custom class contains a certain collection among its data members, the iterator
# will enable the "user" of this class to "iterate" over this collection in a "native"
# manner - i.e. - as if it would have iterate over any Python's built-in collection.
# By implementing an iterator for this class, we will enable the "user" of this class to
# iterate over the "internal" collection of the class.
# NOTE: In case in a certain class there are two "collections" that are candidates to
# be "iterated over", than ONLY one can be chosen eventually.


# some notes:
# ===========
# 1) in this implementation, the self.__counter is NOT thread-safe - i.e. if two threads
# will iterate over the same object at the same time, they are "open" to race conditions.
# 2) the ONLY way to handle the "stop condition" on the __next__ function is to "catch"
# an "StopIteration" exception, that eventually will be thrown.

class Student:

    def __init__(self, name):
        self.name = name
        self.__grades = []
        self.__counter = 0

    def add_grade(self, grade_to_add):
        if grade_to_add > 0:
            self.__grades.append(grade_to_add)

    def __str__(self):
        str_to_ret = self.name + " has the following grades:\n"
        for grade in self.__grades:
            str_to_ret += str(grade) + ","

        return str_to_ret

    def __iter__(self):
        # usually, it simply returning a pointer to self and setting the "pointer" of the
        # counter to the "beginning" of the iterated "list" , which in this case it is
        # the self.__grades array.
        self.__counter = 0
        return self

    def __next__(self):
        if self.__counter < len(self.__grades):
            tmp = self.__grades[self.__counter]
            self.__counter += 1
            return tmp
        else:
            raise StopIteration()


grade1 = 90
grade2 = 89
grade3 = 77
student = Student("Ben")
student.add_grade(grade1)
student.add_grade(grade2)
student.add_grade(grade3)
print(str(student))


def iterate_over_large_file():
    file_name = "someGiantLogFile"
    print(next(open(file_name)))
    print(next(open(file_name)))

iterate_over_large_file()