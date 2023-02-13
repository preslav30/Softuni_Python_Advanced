size = int(input())
car_number = int(input())
matrix = [input().split() for _ in range(size)]
current_position = [0, 0]
total_km = 0
positions_of_tunnel = []
for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'T':
            positions_of_tunnel.append([i, j])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()
    if command == 'End':
        matrix[current_position[0]][current_position[1]] = 'C'
        print(f"Racing car {car_number} DNF.")
        break
    row, col = current_position[0], current_position[1]
    new_row = row + directions[command][0]
    new_col = col + directions[command][1]
    if 0 <= new_row < size and 0 <= new_col < size:
        current_position = [new_row, new_col]
        if matrix[new_row][new_col] == 'T':
            if new_row == positions_of_tunnel[0][0] and new_col == positions_of_tunnel[0][1]:
                current_position = [positions_of_tunnel[1][0], positions_of_tunnel[1][1]]
            else:
                current_position = [positions_of_tunnel[0][0], positions_of_tunnel[0][1]]
            total_km += 30
            matrix[new_row][new_col] = '.'
            matrix[current_position[0]][current_position[1]] = '.'
        elif matrix[new_row][new_col] == '.':
            total_km += 10
        elif matrix[new_row][new_col] == 'F':
            total_km += 10
            print(f'Racing car {car_number} finished the stage!')
            matrix[current_position[0]][current_position[1]] = 'C'
            break
print(f"Distance covered {total_km} km.")
for i in matrix:
    print(*[''.join(i)])
