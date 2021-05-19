'''
Given an array of integers and number K, find the K numbers that appears most in the array and return
them according to descending order
'''


def get_descending_order_k_digits_array_that_appears_most_in_orig_arr(k: int, arr: list) -> list:
    print("got the original array of number:" + str(arr) + ", and number k:" + str(k))
    numbers_dict = {}
    for num in arr:
        if numbers_dict.get(num, None) is not None:
            numbers_dict[num] += 1
        else:
            numbers_dict[num] = 1

    print("numbers_dict is:" + str(numbers_dict))
    appearances_list = sorted(list(numbers_dict.values()), reverse=True)
    k_most_appearances_list = appearances_list[:k]
    print("k_most_appearances list is:" + str(k_most_appearances_list))
    ret_list = []
    amount_of_numbers_added_to_ret_list = 0
    for appearance_val in k_most_appearances_list:
        if amount_of_numbers_added_to_ret_list == k:
            print("done adding numbers to ret_list")
            break

        for key, val in numbers_dict.items():
            if val == appearance_val:
                print("adding " + str(key) + " that appears " + str(val) + " times in the array")
                ret_list.append(key)
                amount_of_numbers_added_to_ret_list += 1
                if amount_of_numbers_added_to_ret_list == k:
                    print("added " + str(k) + " numbers with most appearances, terminating")
                    break

    ret_list = sorted(ret_list, reverse=True)
    return ret_list


k = 3
arr = [1, 7, 4, 5, 3, 7, 1, 5, 9, 8, 5]
expected_ret_arr = [7, 5, 1]
ret_val = get_descending_order_k_digits_array_that_appears_most_in_orig_arr(k, arr)
if ret_val != expected_ret_arr:
    print("the returned list of numbers is:" + str(ret_val) + ", BUT it was expected to be:"
          + str(expected_ret_arr))
    exit(1)

arr = [1, 7, 4, 5, 3, 7, 5, 9, 8, 5]
expected_ret_arr = [7, 5, 1]
ret_val = get_descending_order_k_digits_array_that_appears_most_in_orig_arr(k, arr)
if ret_val != expected_ret_arr:
    print("the returned list of numbers is:" + str(ret_val) + ", BUT it was expected to be:"
          + str(expected_ret_arr))
    exit(1)
