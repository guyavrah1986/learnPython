# I/O
# by default every input that is recived from the user, for instance via the built-in
# input() method is being "read" as string, so, in case the value read needs to be used
# not as a string, for instance as an int, a conversion of its value MUST take place.
# NOTE: it is possible to use the built-in eval() method in order to automatically
# converts it to the "proper" type. Pay attention, however, that in case a string is
# required, then when typing the input, a string MSUT be provided within "".

func_name = "ex_1 - "
user_input = eval(input("Please enter a number:"))

print(func_name + "user entered number:" + str(user_input))

'''
try:
   val = int(user_input)
except ValueError:
   print(func_name + "entered:" + user_input + " which is not an int!")
'''

# array iteration: it is always faster (fasted !!) to iterate over a collection with the
# "for each" flavour
for i in range(4):
    print(i)

arr = [0,1,2,3]
for num in arr:
    print(num)

