from learnPython.questions.questionsUtils import create_sub_string_chars_dict


def permutation_sub_string(str1: str, str2: str) -> bool:
    print("got str1:" + str1 + ", and str2:" + str2)
    str2_chars_dict = create_sub_string_chars_dict(str2)
    print("str2 produces the following dictionary:" + str(str2_chars_dict))

    str1_len = len(str1)
    str2_len = len(str2)
    index = 0
    while index + str2_len < str1_len + 1:
        sub_string_to_check = str1[index:index + str2_len]
        print("about to check if str2 is sub string permutation of:" + sub_string_to_check)
        sub_string_chars_dict = create_sub_string_chars_dict(sub_string_to_check)
        if sub_string_chars_dict == str2_chars_dict:
            print(sub_string_to_check + " is a permutation sub string of:" + str2)
            return True

        index += 1

    return False


str1 = "abcde"
str2 = "rabc"
if permutation_sub_string(str1, str2):
    add_to_output = ""
else:
    add_to_output = "NOT"

output = str2 + " is " + add_to_output + " a permutation sub string of:" + str1
print(output)
