matrix_size = list(map(int, input().split(', ')))
matrix = []
for row in range(matrix_size[0]):
    elements = list(map(int, input().split()))
    matrix.append(elements)

for column in range(matrix_size[1]):
    suma = 0
    for row in matrix:
        suma += row[column]
    print(suma)