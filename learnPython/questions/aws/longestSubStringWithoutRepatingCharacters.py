'''
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
'''


def lengthOfLongestSubstring(s: str) -> int:
    str_len = len(s)
    char_dict = [0] * 128
    right = left = 0
    res = 0
    while right < str_len:
        right_char = s[right]
        char_dict[ord(right_char)] += 1

        while char_dict[ord(right_char)] > 1:
            left_char = s[left]
            char_dict[ord(left_char)] -= 1
            left += 1

        res = max(res, right - left + 1)
        right += 1

    return res


s = "abcabcbb"
expected_ret_val = 3
ret_val = lengthOfLongestSubstring(s)
if expected_ret_val != ret_val:
    print("expected to get:" + str(expected_ret_val) + ", BUT instead got:" + str(ret_val))
    exit(1)

s = "bbbbb"
expected_ret_val = 1
ret_val = lengthOfLongestSubstring(s)
if expected_ret_val != ret_val:
    print("expected to get:" + str(expected_ret_val) + ", BUT instead got:" + str(ret_val))
    exit(1)

s = "pwwkew"
expected_ret_val = 3
ret_val = lengthOfLongestSubstring(s)
if expected_ret_val != ret_val:
    print("expected to get:" + str(expected_ret_val) + ", BUT instead got:" + str(ret_val))
    exit(1)

s = "tmmzuxt"
expected_ret_val = 5
ret_val = lengthOfLongestSubstring(s)
if expected_ret_val != ret_val:
    print("expected to get:" + str(expected_ret_val) + ", BUT instead got:" + str(ret_val))
    exit(1)