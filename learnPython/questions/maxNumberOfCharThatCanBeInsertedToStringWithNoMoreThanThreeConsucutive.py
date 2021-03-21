'''
Given a string, how many characters e.g 'b' can you input in the string so that no 3 consecutive
'b's exist within the string.

Example:
Given: cat
String: bbcbbabbtbb
Output: 8

Given babb
String: bbabb
Output: 1

Given bb
String: bb
Output: 0
'''

def max_num_of_insertion_of_char_to_string_with_no_more_than_three_consucutive_appearnces_of_char(char: str, string: str) -> int:
    print("got the following string:" + string + " and the char:" + char + " to insert into it")
    string_len = len(string)
    index = 1
    num_of_char_insertion = 0

    while index < string_len:
        print("string[" + str(index) + "]:" + string[index])
        if string[index] != char:
            if string[index - 1] != char:
                num_of_char_insertion += 2
            else:
                if index - 2 >= 0 and string[index - 2] == char:
                    print("NOT possible to add " + char + "(s)")
                else:
                    num_of_char_insertion += 1

            index += 1
            continue

        num_of_attached_chars_in_string = 1
        print("so far counted:" + str(num_of_attached_chars_in_string) + " attached " + char)

        index += 1
        while index < string_len and string[index] == char:
            num_of_attached_chars_in_string += 1
            print("so far counted:" + str(num_of_attached_chars_in_string) + " attached " + char)
            index += 1

        # index += 1
        print("eventually, in this loop, counted:" + str(num_of_attached_chars_in_string) + " attached " + char)
        '''
        if num_of_attached_chars_in_string < 2:
            num_of_char_insertion += 1
        '''
    # edge cases:
    # 1) first character
    if string[0] != char:
        num_of_char_insertion += 2
        print("the FIRST char of the string NOT equal to:" + char
              + ",so add two more to the total count")

    # 2) last character
    if string[string_len - 1] != char:
        num_of_char_insertion += 2
        print("the LAST char of the string NOT equal to:" + char
              + ",so add two more to the total count")

    return num_of_char_insertion

char = "b"

string = "bb"
expected_ret_val = 0
ret_val = max_num_of_insertion_of_char_to_string_with_no_more_than_three_consucutive_appearnces_of_char(char, string)
if expected_ret_val != ret_val:
    print("!!!!!! expected ret val of:" + str(expected_ret_val) + ", BUT got:" + str(ret_val) + "!!!!!!")
    exit(1)

string = "ab"
expected_ret_val = 3
ret_val = max_num_of_insertion_of_char_to_string_with_no_more_than_three_consucutive_appearnces_of_char(char, string)
if expected_ret_val != ret_val:
    print("!!!!!! expected ret val of:" + str(expected_ret_val) + ", BUT got:" + str(ret_val) + "!!!!!!")
    exit(1)

string = "ba"
expected_ret_val = 3
ret_val = max_num_of_insertion_of_char_to_string_with_no_more_than_three_consucutive_appearnces_of_char(char, string)
if expected_ret_val != ret_val:
    print("!!!!!! expected ret val of:" + str(expected_ret_val) + ", BUT got:" + str(ret_val) + "!!!!!!")
    exit(1)

string = "cat"
expected_ret_val = 8
ret_val = max_num_of_insertion_of_char_to_string_with_no_more_than_three_consucutive_appearnces_of_char(char, string)
if expected_ret_val != ret_val:
    print("!!!!!!!!! \n expected ret val of:" + str(expected_ret_val) + ", BUT got:" + str(ret_val) + "!!!!!!!!!")
    exit(1)

string = "cbt"
expected_ret_val = 5
ret_val = max_num_of_insertion_of_char_to_string_with_no_more_than_three_consucutive_appearnces_of_char(char, string)
if expected_ret_val != ret_val:
    print("!!!!!! expected ret val of:" + str(expected_ret_val) + ", BUT got:" + str(ret_val) + "!!!!!!!")
    exit(1)

string = "babb"
expected_ret_val = 1
ret_val = max_num_of_insertion_of_char_to_string_with_no_more_than_three_consucutive_appearnces_of_char(char, string)
if expected_ret_val != ret_val:
    print("!!!!!! expected ret val of:" + str(expected_ret_val) + ", BUT got:" + str(ret_val) + "!!!!!!")
    exit(1)