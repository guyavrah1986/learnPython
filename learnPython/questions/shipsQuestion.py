

'''
[ 0 0 0 0 0 ]
[ 1 0 0 1 1 ]
[ 1 0 0 0 0 ]
[ 1 0 1 0 0 ]
[ 0 0 1 0 0 ]
--> here there are 3 ships
'''

def validate_valid_ship_location(row_num: int, col_num: int, matrix_size: int, ships_matrix: object) -> bool:
    # check "above"
    if row_num - 1 >= 0 and row_num - 1 < matrix_size:
        if ships_matrix[row_num - 1][col_num] == 1:
            pass


def find_how_many_ships_in_matrix(ships_matrix: object, matrix_size: int) -> int:
    num_of_ships = 0
    for row_num in range(matrix_size):
        for col_num in range(matrix_size):
            print("checking matrix[" + str(row_num) + "][" + str(col_num) + "]:" + str(ships_matrix[row_num][col_num]))
            if ships_matrix[row_num][col_num] == 0:
                continue


    return num_of_ships

N = 5
# set matrix to all zeros
matrix = [[0]*N for i in range(N)]

# set first line
matrix[1][0] = 1
matrix[1][3] = 1
matrix[1][4] = 1

# set second line
matrix[2][0] = 1

# set third line
matrix[3][0] = 1
matrix[3][2] = 1

# set 4th line
matrix[3][0] = 1

for row_num in range(N):
    for col_num in range(N):
        print("[" + str(matrix[row_num][col_num]) + "]",  end="")
    print("")

num_of_ships = find_how_many_ships_in_matrix(matrix, N)
print("there are " + str(num_of_ships) + " in the ships matrix")
