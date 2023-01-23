matrix_size = list(map(int, input().split(', ')))
matrix = []
suma = 0
for rows in range(matrix_size[0]):
    elements = list(map(int, input().split(', ')))
    matrix.append(elements)

for row in range(matrix_size[0]):
    for column in range(matrix_size[1]):
        if row < matrix_size[0] - 1 and column < matrix_size[1] - 1:

            if matrix[row][column] + matrix[row + 1][column] + matrix[row + 1][column + 1] + matrix[row][column + 1] > suma:
                suma = matrix[row][column] + matrix[row + 1][column] + matrix[row + 1][column + 1] + matrix[row][column + 1]
                submatrix = []
                submatrix.append(matrix[row][column])
                submatrix.append(matrix[row][column + 1])
                submatrix.append(matrix[row + 1][column])
                submatrix.append(matrix[row + 1][column + 1])

print(f'{submatrix[0]} {submatrix[1]}')
print(f'{submatrix[2]} {submatrix[3]}')
print(suma)