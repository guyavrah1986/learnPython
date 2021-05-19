'''

'''


def get_number_after_nine_is_inserted(num: int) -> int:
    print("original number is:" + str(num))
    if num > 0:
        new_num = (9 * 10000) + num
    else:
        new_num = (10 * num) - 9

    return new_num


num = 1234
expected_new_num = 91234
ret_num = get_number_after_nine_is_inserted(num)
if ret_num != expected_new_num:
    print("expected number to be:" + str(expected_new_num) + ", but instead got:" + str(ret_num))
    exit(1)


num = -1234
expected_new_num = -12349
ret_num = get_number_after_nine_is_inserted(num)
if ret_num != expected_new_num:
    print("expected number to be:" + str(expected_new_num) + ", but instead got:" + str(ret_num))
    exit(1)