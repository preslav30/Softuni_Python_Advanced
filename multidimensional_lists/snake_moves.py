from collections import deque

r, c = list(map(int, input().split()))
snake = deque(input())

for row in range(r):
    if row % 2 == 0:
        for i in range(c):
            popped = snake.popleft()
            print(popped, end='')
            snake.append(popped)
        print()
    else:
        roww = ''
        for i in range(c - 1, -1, -1):
            popped = snake.popleft()
            roww += popped
            snake.append(popped)
        print(roww[::-1]) 


