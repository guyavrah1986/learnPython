'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums: list) -> list:
        ret_set = set()
        already_taken = set()
        taken = {}
        for i, curr_num in enumerate(nums):
            if curr_num in already_taken:
                continue

            already_taken.add(curr_num)
            curr_sliced_list = nums[i + 1:]
            for num2 in curr_sliced_list:
                to_zero_sum = 0 - (curr_num + num2)
                if to_zero_sum in taken and taken[to_zero_sum] == i:
                    print("curr num is:" + str(curr_num))
                    print("num2 is:" + str(num2))
                    print("to_zero_sum is:" + str(to_zero_sum))
                    ret_set.add(tuple(sorted((curr_num, num2, to_zero_sum))))

                taken[num2] = i

        return ret_set