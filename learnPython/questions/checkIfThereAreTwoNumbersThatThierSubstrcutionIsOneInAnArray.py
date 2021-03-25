'''
Given an array of integers, return true if there are at least two numbers that one is greater than the
other by 1. Return false otherwise
'''


def check_adjacent_numbers_in_array(arr: list) -> bool:
    print("got the following array of numbers:" + str(arr))
    numbers_in_arr_dict = {}
    for num in arr:
        numbers_in_arr_dict[num] = 1
        if numbers_in_arr_dict.get(num - 1, None) is not None or numbers_in_arr_dict.get(num + 1, None) is not None:
            return True

    return False


arr = [1, 4, 6, 33, 9]
ret_code = check_adjacent_numbers_in_array(arr)
expected_val = True
if ret_code != expected_val:
    print("expected to receive:" + str(expected_val) + " BUT got:" + str(ret_code))
    exit(1)
