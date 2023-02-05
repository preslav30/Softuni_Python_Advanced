# Get the size of the field
size = int(input().strip())

# Read the field matrix
matrix = []
for i in range(size):
    line = input().strip().split()
    matrix.append(line)

# Find the starting position of the bunny
start = None
for i in range(size):
    for j in range(size):
        if matrix[i][j] == "B":
            start = (i, j)
            break
    if start:
        break

# Define the possible directions for moving
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Keep track of the maximum number of eggs collected
max_eggs = 0
max_eggs_direction = None
max_eggs_path = []

# MAIN LOOP Iterate over each direction
for dx, dy in directions:
    x, y = start
    eggs = 0
    path = []
    while 0 <= x < size and 0 <= y < size and matrix[x][y] != "X": # while we are still in the matrix or until we reach an 'X'
        element = matrix[x][y]
        if element != "B":
            eggs += int(element)
            path.append([x, y])
        x += dx  # we increase the direction by the value of itself so that if it is 0, it stays 0, if it is negative, it stays negative
        y += dy
    if eggs > max_eggs:
        max_eggs = eggs
        max_eggs_direction = (dx, dy)
        max_eggs_path = path

# Determine the best direction based on the maximum number of eggs collected
if max_eggs_direction == (-1, 0):
    best_direction = "up"
elif max_eggs_direction == (1, 0):
    best_direction = "down"
elif max_eggs_direction == (0, -1):
    best_direction = "left"
else:
    best_direction = "right"

# Print the result
print(best_direction)
for path in max_eggs_path:
    print(path)
print(max_eggs)

# explanation for MIAIN LOOP
# In the first iteration of the loop, dx and dy are assigned the values of the first pair of the directions list.
# Before we start to check the number of eggs in this direction, we first initialize some variables:
# x, y are set to the starting position of the bunny start, eggs is set to 0 (to keep track of the number of eggs collected),
# and path is set to an empty list (to keep track of the path that the bunny took).
# Next, we have the while loop, which will continue to execute until either the current position is out of bounds of the field, or we have reached a trap ("X").
# In each iteration of the while loop, we first access the item at the current position in the field using the field[x][y] expression.
# If the item is not a trap ("X") or a bunny ("B"), we increment the eggs variable by the value of the item (which is assumed to be a number), and append the current position to the path list.
# After we have processed the current position, we update the x and y coordinates for the next position by adding dx and dy respectively.
