rows, columns = list(map(int, input().split()))
matrix = []
suma = 0

for i in range(rows):
    matrix.append(list(map(int, input().split())))

for row in range(rows - 2):
    for col in range(columns - 2):
        sub_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + matrix[row + 1][
            col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][
            col + 2]
        if sub_sum > suma:
            submatrix = []
            suma = sub_sum
            submatrix.extend([matrix[row][col], matrix[row][col + 1], matrix[row][col + 2], matrix[row + 1][col], matrix[row + 1][
            col + 1], matrix[row + 1][col + 2], matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][
            col + 2]])
print(f'Sum = {suma}')
for i in range(3):
    print(submatrix[i], end=' ')
print()
for i in range(3, 6):
    print(submatrix[i], end=' ')
print()
for i in range(6, 9):
    print(submatrix[i], end=' ')
