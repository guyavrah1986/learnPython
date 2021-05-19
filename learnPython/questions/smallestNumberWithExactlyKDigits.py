'''
Given number N that has K digits, find the smallest number that has also exactly K digits
'''


def find_smallest_k_digits_number(num: int) -> int:
    print("got the original number:" + str(num))
    num_str = str(num)
    num_digits = len(num_str)
    print("the original number has " + str(num_digits) + " digits")
    if num_digits == 1:
        return 0

    x = pow(10, num_digits - 1)
    '''
    If a negative number is the desired value then do the following:

    x = pow(10, num_digits)
    x -= 1
    x = x * -1
    '''
    return x


num = 987
expected_ret_val = 100
ret_val = find_smallest_k_digits_number(num)
if ret_val != expected_ret_val:
    print("expected return value:" + str(expected_ret_val) + ", BUT got instead:" + str(ret_val))
    exit(1)

num = 9
expected_ret_val = 0
ret_val = find_smallest_k_digits_number(num)
if ret_val != expected_ret_val:
    print("expected return value:" + str(expected_ret_val) + ", BUT got instead:" + str(ret_val))
    exit(1)
