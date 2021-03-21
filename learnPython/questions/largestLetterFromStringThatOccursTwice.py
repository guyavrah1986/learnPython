'''
Return largest letter from a string, which occurs twice, once as a small letter and one as a big letter.
For example: 'AaBabc' should return B.
'''


def get_largest_letter_form_string_that_occurs_twice(str_to_check: str) -> str:
    print("got the string:" + str_to_check)
    small_letters_in_string_dict = {}
    capital_letters_ascii_value_list = []
    for letter in str_to_check:
        if letter.isupper():
            capital_letters_ascii_value_list.append(ord(letter))
        else:
            small_letters_in_string_dict[ord(letter)] = 1

    print("after going over all letters in the string, we have the following dictionaries:")
    print("small letters dictionary:" + str(small_letters_in_string_dict))
    capital_letters_set = set(capital_letters_ascii_value_list)
    print("capital_letters_ascii_value_list is:" + str(sorted(capital_letters_set, reverse=True)))
    capital_to_small_letter_ascii_value_offset = 32
    for key in sorted(capital_letters_set, reverse=True):
        print("key:" + str(key) + " is in the capital letters dict")
        respective_small_letter = small_letters_in_string_dict.get(key + capital_to_small_letter_ascii_value_offset, None)
        if respective_small_letter is not None:
            return chr(key)

    return None


str_to_check = "AaBabc"
expected_ret_val = "B"
print("the largest letter that appears twice in the string:" + str_to_check
      + " is:" + str(get_largest_letter_form_string_that_occurs_twice(str_to_check)))
ret_val = get_largest_letter_form_string_that_occurs_twice(str_to_check)
if "B" != str(ret_val):
    print("the return value for string:" + str_to_check + " is NOT correct. Expected:" + expected_ret_val
          + ", BUT got:" + ret_val)

str_to_check = "AaBabC"
expected_ret_val = "B"
print("the largest letter that appears twice in the string:" + str_to_check
      + " is:" + str(get_largest_letter_form_string_that_occurs_twice(str_to_check)))
ret_val = get_largest_letter_form_string_that_occurs_twice(str_to_check)
if "B" != str(ret_val):
    print("the return value for string:" + str_to_check + " is NOT correct. Expected:" + expected_ret_val)

str_to_check = "AaBafC"
expected_ret_val = "A"
print("the largest letter that appears twice in the string:" + str_to_check
      + " is:" + str(get_largest_letter_form_string_that_occurs_twice(str_to_check)))
ret_val = get_largest_letter_form_string_that_occurs_twice(str_to_check)
if expected_ret_val != str(ret_val):
    print("the return value for string:" + str_to_check + " is NOT correct. Expected:" + expected_ret_val)
