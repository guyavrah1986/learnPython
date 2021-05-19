'''
Given an array of N (natural) integers return the largest number K (K>0) only if K and -K exist in
the array, if there's no such number return 0. For example if arr=[4,-4, 3, -3, 2], should return 4,
and arr=[-2,0,0,-3] should return 0. I think the algorithm should solve this in O(N).
'''


def get_largest_num_in_array_that_also_has_minus_value(arr: list) -> int:
    print("got the following list of integers:" + str(arr))
    negative_num_dict = {}
    positive_num_list = []
    for num in arr:
        if num > 0:
            positive_num_list.append(num)
        else:
            negative_num_dict[num] = 1

    print("the negative numbers dictionary is:" + str(negative_num_dict))
    for num in sorted(positive_num_list, reverse=True):
        if num * -1 in negative_num_dict:
            print(str(num * -1) + " is in both the positive and negative list, returning it")
            return num

    return 0


arr = [4, -4, 3, -3, 2]
expected_ret_val = 4
ret_val = get_largest_num_in_array_that_also_has_minus_value(arr)
if ret_val != expected_ret_val:
    print("expected to get number:" + str(expected_ret_val) + ", BUT got instead:" + str(ret_val))

arr = [4, 9, 3, -3, 2]
expected_ret_val = 3
ret_val = get_largest_num_in_array_that_also_has_minus_value(arr)
if ret_val != expected_ret_val:
    print("expected to get number:" + str(expected_ret_val) + ", BUT got instead:" + str(ret_val))

arr = [4, 9, -3, -3, 2]
expected_ret_val = 0
ret_val = get_largest_num_in_array_that_also_has_minus_value(arr)
if ret_val != expected_ret_val:
    print("expected to get number:" + str(expected_ret_val) + ", BUT got instead:" + str(ret_val))
