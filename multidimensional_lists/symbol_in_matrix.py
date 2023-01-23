square_size = int(input())
matrix = []
for i in range(square_size):
    matrix.append(input())
symbol = input()
found = False

for column in range(square_size):
    for row in range(square_size):
        if matrix[column][row] == symbol:
            print(f'({column}, {row})')
            found = True
    if found:
        break
if not found:
    print(f'{symbol} does not occur in the matrix')

# ['ABC', 'DEF', 'X!@']

