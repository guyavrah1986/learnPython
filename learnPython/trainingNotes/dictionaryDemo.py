# dictionary enables us to keep a list of elements in the format of <key,value>
# inherently, it allows a single instance of each key, so trying to add a new entry
# to a dictionary where its key is already present in the dictionary, is not possible.
# dictionary is a MUTABLE object, in the "sense" of the value (!!) of a certain key it holds.
# meaning, it is possible to modify the value kept by a certain key.

my_dict = {"guy": 12, "rotem": 17, "roei": 15}
print("initially the dictionary is:\n" + str(my_dict))

# trying to add a new entry to a NON existing key will be fine:
my_dict["buba"] = 11
print("after adding additional non existing key,value, the dictionary is:\n" + str(my_dict))

# trying to add an entry for an already existing key will not cause any modification
# on the dictionary and will NOT throw any error/exception and will indeed change the
# value of the given key
my_dict["guy"] = 90


# note that in case you wish to remove an entry from a dictionary, you can use the
# built-in del() function.
# NOTE: in case there is no entry in the dict with the provided value to the del() method,
# an exception is thrown.
# del my_dict["bbb"]

# the correct way to do it:
non_exist_key = "bbb"
poped_val = my_dict.pop(non_exist_key, None)
if poped_val is None:
    print(non_exist_key + " is not present as a key in the dictionary, so no deletion was done")

print("after first remove attempt, the dictionary is:\n" + str(my_dict))

exist_key = "rotem"
try:
    del my_dict[exist_key]
except KeyError:
    pass

print("after second remove attempt, the dictionary is:\n" + str(my_dict))
