size = int(input())
territory = [input().split() for _ in range(size)]
collected_teabags = 0
made_it = False
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
for i in range(size):
    for j in range(size):
        if territory[i][j] == 'A':
            alice_position = [i, j]
            territory[i][j] = '*'
        elif territory[i][j].isnumeric():
            territory[i][j] = int(territory[i][j])

while True:
    if collected_teabags >= 10:
        made_it = True
        break
    command = input()
    row = alice_position[0] + directions[command][0]
    col = alice_position[1] + directions[command][1]

    if row < 0 or row >= size or col < 0 or col >= size:
        break

    item = territory[row][col]
    if item not in ['R', '*', '.'] and 0 <= row < size and 0 <= col < size: # and item != 'A':
        collected_teabags += item
        territory[row][col] = '*'
        alice_position = [row, col]
    elif item == 'R':
        territory[row][col] = '*'
        break
    elif item in ['*', '.']:
        territory[row][col] = '*'
        alice_position = [row, col]

if made_it:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for i in territory:
    print(*i)