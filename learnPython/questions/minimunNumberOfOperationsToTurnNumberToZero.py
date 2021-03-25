"""
Given a number represented in a string of its binary form, count the minimal number of operations to
perform on it so it will get to zero. Operations allowed:
1) Divide by 2
2) Substruct 1
"""


def turn_number_to_zero(number: str) -> int:
    print("got the number:" + number)
    return 0


num = "10110101"
decimal_value = int(num, 2)
print("the number in decimal is:" + str(decimal_value))
ret_val = turn_number_to_zero(num)
expected_val = 4
if ret_val != expected_val:
    print("expected return value of:" + str(expected_val) + ", BUT instead got:" + str(ret_val))
    exit(1)

