matrix = [input().split() for _ in range(5)]
commands_count = int(input())
commands_given = 0
player_found = False
total_targets_number = 0
targets_shot = 0
indexes = []
for i in range(5):
    for j in range(5):
        element = matrix[i][j]
        if element == 'A':
            player_position = [i, j]
            player_found = True
        elif element == 'x':
            total_targets_number += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    if targets_shot == total_targets_number:
        print(f"Training completed! All {total_targets_number} targets hit.")
        break
    if commands_given == commands_count:
        print(f"Training not completed! {total_targets_number - targets_shot} targets left.")
        break
    row = player_position[0]
    col = player_position[1]
    command = input().split()
    direction = command[1]
    if command[0] == 'move':
        steps = int(command[2])
        row += directions[direction][0] * steps
        col += directions[direction][1] * steps
        if 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] == '.':
            player_position[0] = row
            player_position[1] = col
    else:
        while True:
            if 0 <= row < 5 and 0 <= col < 5:

                # if row < 0 or row > 4 or col < 0 or col > 4:
                #     break
                if matrix[row][col] == 'x':
                    targets_shot += 1
                    matrix[row][col] = '.'
                    indexes.append([row, col])
                    break
                row += directions[direction][0]
                col += directions[direction][1]
            else:
                break
    commands_given += 1
for x in indexes:
    print(x)
