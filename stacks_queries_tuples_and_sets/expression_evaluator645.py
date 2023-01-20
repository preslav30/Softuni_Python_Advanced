from collections import deque

expression = input().split()
numbers = deque()

for i in expression:
    if i.isdigit() or (len(i) > 1 and i[0] == '-'):
        numbers.append(int(i))

    else:
        while len(numbers) > 1:
            if i == '*':
                result = numbers.popleft() * numbers.popleft()
                numbers.appendleft(result)
            elif i == '/':
                result = numbers.popleft() // numbers.popleft()
                numbers.appendleft(result)
            elif i == '+':
                result = numbers.popleft() + numbers.popleft()
                numbers.appendleft(result)
            elif i == '-':
                result = numbers.popleft() - numbers.popleft()
                numbers.appendleft(result)

print(*numbers)