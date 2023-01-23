matrix_size = list(map(int, input().split(', ')))
suma = 0
matrix = []
for row in range(1, matrix_size[0] + 1):
    elements = list(map(int, input().split(', ')))
    matrix.append(elements)
    suma += sum(elements)

print(suma)
print(matrix)
