'''
Given an array of integers, find the index to which if we insert the number 5, we will get the
largest number.
'''


def get_index_to_which_if_num_is_inserted_then_we_get_largest_number(num_to_insert: int,
                                                                     arr: list) -> int:
    print("got the following array of integers:" + str(arr) + ", and number to insert:" + str(num_to_insert))
    arr_len = len(arr)
    index = 0
    while index < arr_len:
        if arr[index] < num_to_insert:
            return index

        index += 1

    return arr_len


arr = [9, 8, 7, 4, 6]
num_to_insert = 5
expected_ret_val = 3
ret_val = get_index_to_which_if_num_is_inserted_then_we_get_largest_number(num_to_insert, arr)
if ret_val != expected_ret_val:
    print("got ret val:" + str(ret_val) + ", BUT expected to get:" + str(expected_ret_val))
    exit(1)

arr = [1, 2, 3, 4]
expected_ret_val = 0
ret_val = get_index_to_which_if_num_is_inserted_then_we_get_largest_number(num_to_insert, arr)
if ret_val != expected_ret_val:
    print("got ret val:" + str(ret_val) + ", BUT expected to get:" + str(expected_ret_val))
    exit(1)
