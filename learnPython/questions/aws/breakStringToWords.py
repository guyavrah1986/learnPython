'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''

def break_sub_string_to_words(string: str, word_dict: list, start_index: int) -> bool:
    if start_index == len(string):
        return True

    for end_index in range(start_index, len(string) + 1):
        if string[start_index: end_index] in word_dict and break_sub_string_to_words(string, word_dict, end_index):
            return True

    return False


def break_string_to_words(string: str, word_dict: list) -> bool:
    return break_sub_string_to_words(string, word_dict, 0)


word_dict = ["car", "ca", "rs"]
string = "cars"
expected_res = True
ret = break_string_to_words(string, word_dict)
if expected_res != ret:
    print("expected to get:" + str(expected_res) + ", but got:" + str(ret))
    exit(1)


