def two_sum(nums: list, target: int) -> list:
    complementary_dict = {}
    index = 0
    ret_list = []
    arr_len = len(nums)
    while index < arr_len:
        # print("nums[" + str(index) + "]:" + str(nums[index]))
        curr_key = nums[index]
        curr_val = index
        if complementary_dict.get(target - curr_key, None) is not None:
            ret_list.append(curr_val)
            ret_list.append(complementary_dict[target - curr_key])
            return ret_list
        else:
            complementary_dict[curr_key] = curr_val

        index += 1

arr = [2, 7, 12, 3]
target = 9
expected_ret_list = [0, 1]
ret_list = two_sum(arr, target)
if sorted(ret_list) != sorted(expected_ret_list):
    print("was expecting list of the following indices:\n" + str(expected_ret_list) + "\n, but instead got:\n"
          + str(ret_list))
    exit(1)