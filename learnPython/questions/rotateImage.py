'''

'''
from learnPython.questions.questionsUtils import print_two_dim_matrix


def rotate(matrix: list) -> None:
    transpose(matrix)
    reflect(matrix)


def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


def reflect(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]




matrix_to_rotate = [[1,2, 3], [4, 5, 6], [7, 8, 9]]
print("BEFORE rotation the matrix is:\n")
print_two_dim_matrix(matrix_to_rotate)
rotate(matrix_to_rotate)
print("AFTER rotation the matrix is:\n")
print_two_dim_matrix(matrix_to_rotate)