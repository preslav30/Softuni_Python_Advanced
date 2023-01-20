from collections import deque

bees = deque(map(int, (input().split())))
nectars = deque(map(int, (input().split())))
symbols = deque(input().split())
total_honey = 0

while nectars and bees:
    bee = bees[0]
    nectar = nectars[-1]
    if nectar >= bee:
        symbol = symbols[0]
        if symbol == '+':
            total_honey += abs(bee + nectar)
        elif symbol == '-':
            total_honey += abs(bee - nectar)
        elif symbol == '*':
            total_honey += abs(bee * nectar)
        elif symbol == '/':
            total_honey += abs(bee / nectar)
        bees.popleft()
        nectars.pop()
        symbols.popleft()
    else:
        nectars.pop()
        continue

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: ", end='')
    print(*bees, sep=', ')
if nectars:
    print(f"Nectar left: ", end='')
    print(*nectars, sep=', ')