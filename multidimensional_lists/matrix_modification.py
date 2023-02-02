rows = int(input())
matrix = [list(map(int, input().split())) for rowss in range(rows)]

while True:
    command = input()
    if command == 'END':
        break
    action, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[0]) - 1:
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in range(len(matrix)):
    for col in matrix[row]:
        print(col, end=' ')
    print()