'''
Given an array of positive integers and number K, find K elements in the array that their sum is
the largest.
'''


def get_max_sum_of_k_elements_in_array(arr: list, k: int) -> int:
    print("the array is:" + str(arr) + " and K is:" + str(k))
    max_sum = 0
    num_of_numbers_added = 0
    sorted_array = sorted(arr, reverse=True)
    while num_of_numbers_added < k:
        max_sum += sorted_array[num_of_numbers_added]
        num_of_numbers_added += 1

    return max_sum


arr = [3, 4, 5, 7, 1, 9, 7, 8, 4, 5]
k = 3
expected_ret_sum = 9 + 8 + 7
ret_sum = get_max_sum_of_k_elements_in_array(arr, k)
if ret_sum != expected_ret_sum:
    print("expected sum:" + str(expected_ret_sum) + ", but instead got:" + str(ret_sum))
    exit(1)
