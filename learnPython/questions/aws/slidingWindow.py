'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
from collections import deque


def clean_deq(index: int, k: int, deq_to_clean: deque, nums: list) -> None:
    if deq_to_clean and deq_to_clean[0] == index - k:
        deq_to_clean.popleft()

    while deq_to_clean and nums[index] > nums[deq_to_clean[-1]]:
        deq_to_clean.pop()

def get_max_sliding_window_list(arr: list, k: int) -> list:
    # edge cases go here
    ret_list = []

    # initiate the queue with the first K elements
    deq = deque()
    max_index = 0
    for i in range(k):
        clean_deq(i, k, deq, arr)
        deq.append(i)
        if arr[i] > arr[max_index]:
            max_index = i

    ret_list.append(arr[max_index])
    n = len(arr)
    for i in range(k, n):
        clean_deq(i, k, deq, arr)
        deq.append(i)
        ret_list.append(arr[deq[0]])

    return ret_list

orig_list = [1, 3, -1, -3, 5, 3, 6, 7]
expected_ret_list = [3, 3, 5, 5, 6, 7]
k = 3
ret_list = get_max_sliding_window_list(orig_list, k)
if ret_list != expected_ret_list:
    print("expected to receive list:" + str(expected_ret_list) + ", but got:" + str(ret_list))
    exit(1)

