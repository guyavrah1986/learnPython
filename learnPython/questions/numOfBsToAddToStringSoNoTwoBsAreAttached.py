'''
Given a string s that might contain "b"'s, find the maximum number of "b"'s that can be added to the
string so that there won't be more than two consecutive b's in the final string
'''


def get_num_of_b_that_can_be_added_with_having_three_consecutive(orig_str: str) -> int:
    """
    Assumptions:
    a) orig_str does NOT contain 3 b's attached
    """
    print("=====================\nthe original string is:" + orig_str + "\n=====================")
    num_b_to_insert = 0
    index = 0
    prev_letter_was_b = False
    str_len = len(orig_str)
    if orig_str[index] == "b":
        if index < str_len - 1 and orig_str[index + 1] != "b":
            print("first letter is b, and the next letter is NOT, so add 1")
            num_b_to_insert += 1

        prev_letter_was_b = True
    else:
        num_b_to_insert += 2
        print("first letter is NOT b, so add 2. num_b_to_insert:" + str(num_b_to_insert))

    index = 1
    while index < str_len:
        print("checking orig_str[" + str(index) + "]:" + orig_str[index])
        if orig_str[index] != "b":
            print("current letter is NOT b")
            if not prev_letter_was_b:
                print("previous letter was NOT b, so add 2")
                num_b_to_insert += 2
                print("num_b_to_insert:" + str(num_b_to_insert))

            prev_letter_was_b = False
        else:  # s[index] == "b"
            print("current letter is b")
            if prev_letter_was_b:
                print("previous letter was b, so do NOT add another one")
            else:
                if index < str_len - 1 and orig_str[index + 1] != "b":
                    print("previous letter was NOT b, and the next letter is also NOT, so add 1")
                    num_b_to_insert += 1

            prev_letter_was_b = True

        index += 1

    if orig_str[str_len - 1] != "b":
        print("last letter in the string is NOT be, so add 2")
        num_b_to_insert += 2
        print("num_b_to_insert is:" + str(num_b_to_insert))
    else:
        print("last letter is b, so add 1 for the b that can be inserted BEFORE it")
        num_b_to_insert += 1

    return num_b_to_insert


orig_str = "aaa"
expected_ret_val = 8
ret_val = get_num_of_b_that_can_be_added_with_having_three_consecutive(orig_str)
if ret_val != expected_ret_val:
    print("expected to get " + str(expected_ret_val) + " BUT got instead " + str(ret_val))
    exit(1)

orig_str = "aa"
expected_ret_val = 6
ret_val = get_num_of_b_that_can_be_added_with_having_three_consecutive(orig_str)
if ret_val != expected_ret_val:
    print("expected to get " + str(expected_ret_val) + " BUT got instead " + str(ret_val))
    exit(1)

orig_str = "ba"
expected_ret_val = 3
ret_val = get_num_of_b_that_can_be_added_with_having_three_consecutive(orig_str)
if ret_val != expected_ret_val:
    print("expected to get " + str(expected_ret_val) + " BUT got instead " + str(ret_val))
    exit(1)

orig_str = "ab"
expected_ret_val = 3
ret_val = get_num_of_b_that_can_be_added_with_having_three_consecutive(orig_str)
if ret_val != expected_ret_val:
    print("expected to get " + str(expected_ret_val) + " BUT got instead " + str(ret_val))
    exit(1)

orig_str = "b"
expected_ret_val = 1
ret_val = get_num_of_b_that_can_be_added_with_having_three_consecutive(orig_str)
if ret_val != expected_ret_val:
    print("expected to get " + str(expected_ret_val) + " BUT got instead " + str(ret_val))
    exit(1)

orig_str = "a"
expected_ret_val = 4
ret_val = get_num_of_b_that_can_be_added_with_having_three_consecutive(orig_str)
if ret_val != expected_ret_val:
    print("expected to get " + str(expected_ret_val) + " BUT got instead " + str(ret_val))
    exit(1)

orig_str = "bbab"
expected_ret_val = 1
ret_val = get_num_of_b_that_can_be_added_with_having_three_consecutive(orig_str)
if ret_val != expected_ret_val:
    print("expected to get " + str(expected_ret_val) + " BUT got instead " + str(ret_val))
    exit(1)

