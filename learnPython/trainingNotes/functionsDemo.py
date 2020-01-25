
# this is an example for the "named argument" concept in Python. In case there are
# several default arguments, then upon a call to it, it is possible to send only
# some (one or more) specific values.
# Note that this is also true for functions that do not have default arguments at all
# --> this is usually very beneficial for documentation purposes.

def do(num1=4, num2 =6):
    return num1 + num2


res = do(num2=5)
print("res is:" + str(res))

# when working with global variables and we wish to change/alter the value of the global
# variable within an "inner" scope, for instance, within some function, then before using
# the global variable in the "inner scope" there is a need to "declares" that this variable
# is global --> only like so, the the usage in the variable will be indeed with the global
# variable, and not in another variable of the function with the "same" name
num = 90

def change_global_var():
    global num
    num = 12

change_global_var()

print("after change (global) num is:" + str(num))

# anonymous function - in Python it is possible to define such function by
# using the lambda expression keyword
# it is used, among other cases, for the "map-reduce" paradigm
# its main "advantage" is that this implementation keeps track of all the return values
# and keep them in an array (list). It also saved the "definition" of the function.
# the below code section is the "map" part of the "map-reduce" paradigm
from functools import reduce
arr = [1,3,5]
res_arr = list(map(lambda x:x * 2, arr))
print(res_arr)

# in contrast to the map function, the reduce function returns only a single value, which
# is basically the agrgation of the
arr_reduce = [3,4,9]
total = reduce(lambda x,y: x + y, arr_reduce)
print("the total sum of the array to reduce:" + str(total))

# another built-in capability function is the filter
arr_to_filter = [1,55,6,23]
print("original list:" + str(arr_to_filter))
filtered_list = list(filter(lambda x: x > 7, arr_to_filter))
print("filtered list:" + str(filtered_list))