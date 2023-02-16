size = 6
matrix = [input().split() for _ in range(6)]
current_position = [int(_) for _ in list(input()) if _.isdigit()]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    data = input()
    if data == 'Stop':
        break
    data = data.split(', ')
    command, direction = data[0], data[1]
    new_row = directions[direction][0] + current_position[0]
    new_col = directions[direction][1] + current_position[1]
    if 0 <= new_row < 6 and 0 <= new_col < 6:
        if command == 'Create':
            value = data[2]
            if matrix[new_row][new_col] == '.':
                matrix[new_row][new_col] = value
        elif command == 'Update':
            value = data[2]
            if matrix[new_row][new_col].isalnum():
                matrix[new_row][new_col] = value
        elif command == 'Delete':
            if matrix[new_row][new_col].isalnum():
                matrix[new_row][new_col] = '.'
        elif command == 'Read':
            if matrix[new_row][new_col].isalnum():
                print(matrix[new_row][new_col])
        current_position = [new_row, new_col]

for i in matrix:
    print(*i)