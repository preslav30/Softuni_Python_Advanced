from collections import deque

eggs = deque(map(int, input().split(', ')))
paper = deque(map(int, input().split(', ')))
boxes = 0

while eggs and paper:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    elif egg == 13:
        first = paper.popleft()
        last = paper.pop()
        paper.append(first)
        paper.appendleft(last)
        continue
    pap = paper.pop()
    suma = egg + pap
    if suma <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in [*eggs]])}")
if paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in [*paper]])}")