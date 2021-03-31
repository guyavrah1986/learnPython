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

# O(N^2)
def get_max_sub_array(nums: list) -> int:
    max_subarray = -math.inf
    for i in range(len(nums)):
        current_subarray = 0
        for j in range(i, len(nums)):
            current_subarray += nums[j]
            max_subarray = max(max_subarray, current_subarray)

    return max_subarray


# Kaden algorithm (greedy algorithm)
def maxSubArray(self, nums: list) -> int:
    # Initialize our variables using the first element.
    current_subarray = max_subarray = nums[0]

    # Start with the 2nd element since we already used the first one.
    for num in nums[1:]:
        # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)

    return max_subarray