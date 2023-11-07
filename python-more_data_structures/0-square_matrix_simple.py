#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create an empty result matrix with the same dimensions as the input matrix
    result = [[0 for num in row] for row in matrix]
    # Iterate through the rows and columns of the input matrix
    for i in range(len(matrix)):

        for j in range(len(matrix[i])):
            # Square the value and store it in the result matrix
            result[i][j] = matrix[i][j] ** 2

    return result
