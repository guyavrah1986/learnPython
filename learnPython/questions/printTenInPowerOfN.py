'''
Write a function that receives int n and print 10^n.
'''


def print_ten_in_power_of_n(n: int):
    print("got the number " + str(n))
    base = 10
    while n - 1 > 0:
        base *= 10
        n -= 1

    print("base is:" + str(base))


number = 3
print_ten_in_power_of_n(number)