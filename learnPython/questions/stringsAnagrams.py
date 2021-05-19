
def create_sub_string_chars_dict(self, sub_string: str) -> dict:
    ret_dict = {}
    for c in sub_string:
        ret_dict[c] = 1

    return ret_dict


def check_anagram_strings(self, s: str, p: str) -> list:
    print("s is:" + s + ", p is:" + p)
    ret_list = []
    len_s = len(s)
    len_p = len(p)
    if len_p > len_s:
        print("the anagram string is longer than the original string, aborting")
        return ret_list

    p_string_dict = self.create_sub_string_chars_dict(p)
    print("the dictionary for the p string is:" + str(p_string_dict))
    index = 0
    while index <= (len_s - len_p):
        print("processing char[" + str(index) + "]:" + s[index])
        sub_string_to_check = s[index:index + len_p]
        print("about to check sub string:" + sub_string_to_check)
        sub_string_dict = self.create_sub_string_chars_dict(sub_string_to_check)
        print("the dictionary for sub string:" + sub_string_to_check + ", is:" + str(sub_string_dict))
        if sub_string_dict == p_string_dict:
            ret_list.append(index)

        index += 1

    return ret_list


def is_anagram(self, s: str, t: str) -> bool:
    print("s is:" + s + ", t is:" + t)
    len_s = len(s)
    len_t = len(t)
    if len_t < len_s:
        print("the anagram string is shorter than the original string, aborting")
        return False

    t_string_dict = self.create_sub_string_chars_dict(t)
    print("the dictionary for the t string is:" + str(t_string_dict))
    index = 0
    while index <= (len_s - len_t):
        print("processing char[" + str(index) + "]:" + s[index])
        sub_string_to_check = s[index:index + len_t]
        print("about to check sub string:" + sub_string_to_check)
        sub_string_dict = self.create_sub_string_chars_dict(sub_string_to_check)
        print("the dictionary for sub string:" + sub_string_to_check + ", is:" + str(sub_string_dict))
        if sub_string_dict == t_string_dict:
            return True

        index += 1

    return False
