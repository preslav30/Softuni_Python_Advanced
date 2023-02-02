board_size = int(input())
board = [list(input()) for i in range(board_size)]
moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]] # possible moves for a knight
removed = 0

while True: # remove the knight with the most attacks at each iteration. then loop again until there are no more such knights
    max_attacks = 0  # the knight with the most attacks
    max_row = 0  # position of the knight with the most attacks
    max_col = 0
    for row in range(board_size):   # for each row and for each column
        for col in range(board_size):
            if board[row][col] == 'K':  # if the current position contains a knight
                attacks = 0             # current knight's attacks start at 0
                for move in moves:      # for each possible move of the knight
                        new_row, new_col = row + move[0], col + move[1] # calculate the new board position of the current knight for each possible move
                        if 0 <= new_row < board_size and 0 <= new_col < board_size:
                            if board[new_row][new_col] == 'K':              # if the new move contains another knight, increase the current knights attacks by 1
                                attacks += 1
                if attacks > max_attacks:
                    max_attacks = attacks
                    max_row = row
                    max_col = col
    if max_attacks != 0:
        board[max_row][max_col] = '0'
        removed += 1
    else:
        break
print(removed)
