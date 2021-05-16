


def int_to_roman(num: int) -> str:
    digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
              (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
              (5, "V"), (4, "IV"), (1, "I")]

    ret_string = ""
    for value, symbol in digits:
        if num == 0:
            break

        count, num = divmod(num, value)
        # Append "count" copies of "symbol" to roman_digits.
        ret_string += symbol * count

    return ret_string


num = 671
expected_string = "DCLXXI"
ret_string = int_to_roman(num)
if ret_string != expected_string:
    print("the returned string:" + ret_string + " is not as expected:" + expected_string)
    exit(1)