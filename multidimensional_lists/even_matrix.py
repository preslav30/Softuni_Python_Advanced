rows = int(input())
matrix = []
for row in range(rows):
    elements = list(map(int, input().split(', ')))
    for element in range(len(elements) - 1, -1, -1):
        detail = elements[element]
        if elements[element] % 2 != 0 or elements[element] < 2:
            elements.pop(element)
    matrix.append(elements)
print(matrix)
