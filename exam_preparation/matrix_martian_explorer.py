matrix = [input().split() for _ in range(6)]
rover_pos = []
rover_found = False
c = False
m = False
w = False
for i in range(6):
    for j in range(6):
        if matrix[i][j] == 'E':
            rover_pos = [i, j]
            rover_found = True
            break
    if rover_found:
        break

coordinates = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def deposit_found(row, col, deposit):
    print(f'{deposits[deposit]} deposit found at ({row}, {col})')
    # deposit_found(row, col, deposits[deposit][0])


def rock(row, col):
    print(f'Rover got broken at ({row}, {col})')
    if m and c and w:
        print(f'Area suitable to start the colony.')
    else:
        print("Area not suitable to start the colony.")
    quit()


deposits = {
    'W': 'Water',
    'M': 'Metal',
    'C': 'Concrete',
    'R': 'Rock',
}

directions = input().split(', ')

for direction in directions:
    row, col = rover_pos[0] + coordinates[direction][0], rover_pos[1] + coordinates[direction][1]
    if 0 <= row < 6 and 0 <= col < 6:
        if matrix[row][col] in ['W', 'M', 'C']:
            if matrix[row][col] == 'W':
                w = True
            elif matrix[row][col] == 'M':
                m = True
            elif matrix[row][col] == 'C':
                c = True
            deposit_found(row, col, matrix[row][col])
        elif matrix[row][col] == 'R':
            rock(row, col)
        rover_pos = [row, col]
    else:
        if direction == 'up':
            row = 5
        elif direction == 'down':
            row = 0
        elif direction == 'left':
            col = 5
        elif direction == 'right':
            col = 0
        if matrix[row][col] in ['W', 'M', 'C']:
            if matrix[row][col] == 'W':
                w = True
            elif matrix[row][col] == 'M':
                m = True
            elif matrix[row][col] == 'C':
                c = True
            deposit_found(row, col, matrix[row][col])
        elif matrix[row][col] == 'R':
            rock(row, col)
        rover_pos = [row, col]

if m and c and w:
    print(f'Area suitable to start the colony.')
else:
    print("Area not suitable to start the colony.")
