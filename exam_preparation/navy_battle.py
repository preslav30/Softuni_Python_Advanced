size = int(input())
matrix = [list(input()) for i in range(size)]
submarine_position = []
sub_found = False
mines_hit = 0
battlecruisers_remaining = 3
too_many_mines = False
all_cruisers_destroyed = False

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'S':
            submarine_position = [i, j]
            matrix[i][j] = '-'
            sub_found = True
            break
    if sub_found:
        break

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    direction = input()
    row = submarine_position[0]
    col = submarine_position[1]
    new_row = row + directions[direction][0]
    new_col = col + directions[direction][1]
    if 0 <= new_col < size and 0 <= new_row < size:
        if matrix[new_row][new_col] == '*':
            mines_hit += 1
            matrix[new_row][new_col] = '-'

        elif matrix[new_row][new_col] == 'C':
            battlecruisers_remaining -= 1
            matrix[new_row][new_col] = '-'
        submarine_position = [new_row, new_col]
    if mines_hit == 3:
        matrix[new_row][new_col] = 'S'
        too_many_mines = True
        break
    if battlecruisers_remaining == 0:
        matrix[new_row][new_col] = 'S'
        all_cruisers_destroyed = True
        break

if too_many_mines:
    print(f'Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!')
elif all_cruisers_destroyed:
    print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
for i in matrix:
    print(*[''.join(i)])