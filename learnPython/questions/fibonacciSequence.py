

def get_fibonacci_sequence(num_of_elements_in_the_sequence: int) -> list:
    print("need to create first " + str(num_of_elements_in_the_sequence) + " elements in the"
          + " fibonnaci sequence")
    ret_list = []
    prev_prev_element = 0
    prev_element = 1

    ret_list.append(prev_prev_element)
    ret_list.append(prev_element)
    for i in range(num_of_elements_in_the_sequence - 2):
        curr_element = prev_element + prev_prev_element
        prev_prev_element = prev_element
        prev_element = curr_element
        ret_list.append(curr_element)

    return ret_list

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
num_elements = 4
expected_element_list = [0, 1, 1, 2]
ret_list = get_fibonacci_sequence(num_elements)
if ret_list != expected_element_list:
    print("expected list:" + str(expected_element_list) + ", instead got:" + str(ret_list))