class Solution:
    def myAtoi(self, s: str) -> int:
        if s is None or not s:
            return 0

        str_len = len(s)
        # 1) skip leading whitespaces
        curr_index = 0
        while curr_index < str_len and s[curr_index] == " ":
            curr_index += 1

        print("after skipping leading whitespace the string that is left to parse is:"
              + s[curr_index:])
        if curr_index == str_len:
            return 0

        # 2) check if there is a sign
        if s[curr_index] == "-":
            sign = "-"
            curr_index += 1
        elif s[curr_index] == "+":
            sign = "+"
            curr_index += 1
        elif not s[curr_index].isdigit():
            return 0
        else:
            sign = "+"

        print("character at index:" + str(curr_index) + " is the first digit reached")
        if curr_index == str_len:
            print("there were no digits in the original string")
            return 0

        # 3) parse digits until the first non-digit character
        start_number_index = curr_index
        print("the number to convert start at index:" + str(start_number_index))

        while curr_index < str_len and s[curr_index].isdigit():
            curr_index += 1

        # if we got here, then we hit the first non digit character after a sequence of digits
        sub_string_with_num_to_convert = s[start_number_index: curr_index]
        print("the number part in the string is:" + sub_string_with_num_to_convert)

        # 4) go from the end of the string and multiply the digit value by 10^iter_num
        res = 0
        multiplier = 0
        end_number_index = curr_index - 1
        len_num = curr_index - start_number_index
        print(
            "the lenght of the number is:" + str(len_num) + " and its last digits is at index:" + str(end_number_index))
        while len_num > 0:
            curr_digit_as_num = int(s[end_number_index])
            print("current digit as number is:" + str(curr_digit_as_num))
            res += curr_digit_as_num * (pow(10, multiplier))
            multiplier += 1
            len_num -= 1
            end_number_index -= 1

        print("the result is:" + str(res))
        if sign == "-":
            res = res * (-1)

        print("result after considering the sign is:" + str(res))
        if sign == "-":
            if res < (-1) * (pow(2, 31) - 1):
                res = (-1) * (pow(2, 31))
        else:
            if res > (pow(2, 31) - 1):
                res = pow(2, 31) - 1

        return res
