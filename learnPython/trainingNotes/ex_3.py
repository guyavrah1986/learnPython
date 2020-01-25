arr = [[32,15], [1,7,12], [8,4,6,11]]
sum_arr = [0, 0, 0]

sub_arr_num = 0
for sub_arr in arr:
    sub_arr_sum = 0
    for num in sub_arr:
        sub_arr_sum += num
        print(num)

    sum_arr[sub_arr_num] = sub_arr_sum
    sub_arr_num += 1

for sub_arr_sum_index in range(len(sum_arr)):
    print("sum of sub array " + str(sub_arr_sum_index) + ":" + str(sum_arr[sub_arr_sum_index]))