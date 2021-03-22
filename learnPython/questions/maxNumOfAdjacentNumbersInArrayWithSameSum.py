'''
Given an array of integers, return the maximum number of adjacent numberin the array that thier sum
is equal.
'''


def get_max_num_of_adjacent_numbers_with_same_sum(arr: list) -> int:
    print("got the following array of integers:" + str(arr))
    sums_dict = {}
    index = 0
    arr_len = len(arr)
    for index in range(arr_len - 1):
        print("checking arr[" + str(index) + "] and arr[" + str(index + 1) + "]")
        curr_pair_sum = arr[index] + arr[index + 1]
        if sums_dict.get(curr_pair_sum, None) is not None:
            sums_dict[curr_pair_sum] += 1
        else:
            sums_dict[curr_pair_sum] = 1

    sorted_sums_list = sorted(sums_dict.values(), reverse=True)
    return sorted_sums_list[0]


arr = [1, 4, 5, 0, 13, 7, 2, 3]
expected_val = 3
ret_val = get_max_num_of_adjacent_numbers_with_same_sum(arr)
if ret_val != expected_val:
    print("expected to get:" + str(expected_val) + ", BUT got:" + str(ret_val))
    exit(1)
