import collections


class Solution:
    def longestPalindrome(self, s):
        ans = 0
        chars_appearances_dict = {}
        for c in s:
            if chars_appearances_dict.get(c, None) is not None:
                chars_appearances_dict[c] += 1
            else:
                chars_appearances_dict[c] = 1

        for val in chars_appearances_dict.values():
            ans += int(val / 2) * 2
            if ans % 2 == 0 and val % 2 == 1:
                ans += 1
        return ans