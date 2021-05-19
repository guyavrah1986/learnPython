def create_sub_string_chars_dict(sub_string: str) -> dict:
    ret_dict = {}
    for c in sub_string:
        if c in ret_dict:
            ret_dict[c] += 1
        else:
            ret_dict[c] = 1

    return ret_dict

def print_two_dim_matrix(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
