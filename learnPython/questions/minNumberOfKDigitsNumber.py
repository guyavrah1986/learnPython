'''
number digit-manipulation (classic division): Input of k-digits, return the min number of k digits
'''


def get_min_digit_of_number(number: int) -> int:
    print("got the following number:" + str(number))
    digits_list = []
    digits_dict = {}
    while number > 0:
        digit = number % 10
        number = int(number / 10)
        print("after dividing by 10, number is:" + str(number))
        print("added digit:" + str(digit))
        digits_dict[digit] = 1
        #digits_list.append(digit)

    for i in range(10):
        if i in digits_dict:
            return i
        
    return 0


number = 1923
expected_ret_val = 1
ret_val = get_min_digit_of_number(number)
if expected_ret_val != ret_val:
    print("expected to get number:" + str(expected_ret_val) + ", but instead got:" + str(ret_val))