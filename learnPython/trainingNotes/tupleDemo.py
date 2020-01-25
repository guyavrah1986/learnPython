# differently from collection, tuples can not be modified
# highly used as a return value form function that needs to return more than a single value.

def ret_tuple(num1, num2):
    my_tuple = (num1, num2)
    return my_tuple

my_tuple = ret_tuple(12,45)
print(my_tuple)

