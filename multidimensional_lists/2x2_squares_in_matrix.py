rows, columns = list(map(int, input().split()))
matrix = []
submatrices = 0


for i in range(rows):
    matrix.append(input().split())

for row in range(rows):
    for column in range(columns):
        if row < rows - 1 and column < columns - 1:
            if matrix[row][column] == matrix[row + 1][column] == matrix[row + 1][column + 1] == matrix[row][column + 1]:
                submatrices += 1
print(submatrices)