square_size = int(input())

matrix = []
suma = 0
for i in range(square_size):
    rows = list(map(int, input().split()))
    matrix.append(rows)
for column in range(square_size):
    for row in range(square_size):
        if column == row:
            suma += matrix[row][column]
print(suma)

