"""
Given a number represented in a string of its binary form, count the minimal number of operations to
perform on it so it will get to zero. Operations allowed:
1) Divide by 2
2) Substruct 1
"""


def turn_number_to_zero(number: str) -> int:
    print("got the number:" + number)
    str_len = len(number)
    num_of_operations_needed = 0
    if str_len == 0:
        print("empty number")
        return num_of_operations_needed

    while str_len > 0:
        print("number is:" + number + "(" + str(int(number, 2)) + " in decimal)")
        print("checking number[" + str(str_len - 1) + "]:" + str(number[str_len - 1]))
        # subtract by 1 is needed
        if number[str_len - 1] == "1":
            print("LSB digit is one, increment the number of operations, change it to zero, and move on")
            number = number[: str_len - 1] + "0"
            print("after changing the last digit, number is:" + number)
        else:
            print("number[" + str(str_len - 1) + "] is zero, traversing the number till reaching 1")
            while str_len > 0 and number[str_len - 1] == "0":
                str_len -= 1
                num_of_operations_needed += 1

            number = number[: str_len]
            print("after sub string number is:" + number)

    return num_of_operations_needed


def calculate_(s):
    # if the size of binary is 1
    # then the number of actions will be zero
    if len(s) == 1:
        return 0

    # initializing the number of actions as 0 at first
    count_ = 0
    i = len(s) - 1
    while i > 0:

        # start traversing from the last digit
        # if its 0 increment the count and decrement i
        if s[i] == '0':
            count_ += 1
            i -= 1

            # if s[i] == '1'
        else:
            count_ += 1

            # stop until you get 0 in the binary
            while s[i] == '1' and i > 0:
                count_ += 1
                i -= 1
            if i == 0:
                count_ += 1
            # when encounter a 0 replace it with 1
            s = s[:i] + "1" + s[i + 1:]
    return count_


num = "10000100000"
decimal_value = int(num, 2)
print("the number in decimal is:" + str(decimal_value))
ret_val = calculate_(num)
expected_val = 4
if ret_val != expected_val:
    print("expected return value of:" + str(expected_val) + ", BUT instead got:" + str(ret_val))
    exit(1)

