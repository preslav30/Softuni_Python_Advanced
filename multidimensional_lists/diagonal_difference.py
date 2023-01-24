rows = int(input())
matrix = []
primary = 0
secondary = 0
prim_diag = []
sec_diag = []

for i in range(rows):
    matrix.append(list(map(int, input().split())))

for row in range(rows):
    for column in range(rows):
        if row == column:
            prim_diag.append(matrix[row][column])
            primary += matrix[row][column]

for r in range(rows):
    for c in range(rows - 1, -1, -1):
        if r == rows - c - 1:
            sec_diag.append(matrix[r][c])
            secondary += matrix[r][c]

print(abs(primary - secondary))
