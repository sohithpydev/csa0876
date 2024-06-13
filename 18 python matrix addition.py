def matrix_addition(matrix1, matrix2):
    result_matrix = []
    
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None
    
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)
    
    return result_matrix

# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Perform matrix addition
result = matrix_addition(matrix1, matrix2)

# Display the result
if result:
    print("Resultant Matrix after Addition:")
    for row in result:
        print(row)
