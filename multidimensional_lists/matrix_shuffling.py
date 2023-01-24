r, c = list(map(int, input().split()))
matrix = []
for i in range(r):
    matrix.append(input().split())

while True:
    command = input().split()
    if command[0] == 'END':
        break
    if command[0] != 'swap':
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
    if row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0 or row1 > r - 1 or col1 > c - 1 or row2 > r - 1 or col2 > c - 1:
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for i in matrix:
        for el in i:
            print(el, end=' ')
        print()

