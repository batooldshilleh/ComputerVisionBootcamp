def multiply_matrices(mat1, mat2):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result

def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant_3x3(matrix):
    det = 0
    for i in range(3):
        det += matrix[0][i] * determinant_2x2([[matrix[1][(i+1)%3], matrix[1][(i+2)%3]],
                                                 [matrix[2][(i+1)%3], matrix[2][(i+2)%3]]])
    return det

def inverse_3x3(matrix):
    det = determinant_3x3(matrix)
    if det == 0:
        raise ValueError("Matrix is singular, cannot find inverse.")
    
    adjugate = [[0] * 3 for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            cofactor = determinant_2x2([[matrix[(i+1)%3][(j+1)%3], matrix[(i+1)%3][(j+2)%3]],
                                         [matrix[(i+2)%3][(j+1)%3], matrix[(i+2)%3][(j+2)%3]]])
            adjugate[j][i] = ((-1) ** (i + j)) * cofactor
    
    inverse = [[element / det for element in row] for row in adjugate]
    
    return inverse

mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result_product = multiply_matrices(mat1, mat2)
print("Matrix Product:")
for row in result_product:
    print(row)

result_det_2x2 = determinant_2x2([[4, 3], [2, 1]])
print("\nDeterminant of 2x2 Matrix:", result_det_2x2)

result_det_3x3 = determinant_3x3([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print("\nDeterminant of 3x3 Matrix:", result_det_3x3)

result_inverse_3x3 = inverse_3x3([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print("\nInverse of 3x3 Matrix:")
for row in result_inverse_3x3:
    print(row)

