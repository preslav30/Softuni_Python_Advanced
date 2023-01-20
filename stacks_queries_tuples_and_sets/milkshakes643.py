from collections import deque

chocolate = deque(map(int, input().split(', ')))
milk = deque(map(int, input().split(', ')))
milkshakes = 0

while milkshakes != 5 and milk and chocolate:

    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue

    if chocolate[-1] == milk[0]:
        chocolate.pop()
        milk.popleft()
        milkshakes += 1
    else:
        milk.append(milk.popleft())
        chocolate[-1] -= 5
if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolate:
    print(f'Chocolate: ', end='')
    print(*chocolate, sep=', ')
else:
    print('Chocolate: empty')
if milk:
    print(f'Milk: ', end='')
    print(*milk, sep=', ')
else:
    print('Milk: empty')