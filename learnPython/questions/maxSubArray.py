'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
'''
import math


def get_max_sub_array(nums: list) -> int:
    max_subarray = -math.inf
    for i in range(len(nums)):
        current_subarray = 0
        for j in range(i, len(nums)):
            current_subarray += nums[j]
            max_subarray = max(max_subarray, current_subarray)

    return max_subarray