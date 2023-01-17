from collections import deque

sequence = deque(input())
open_parentheses = deque()
if len(sequence) % 2 != 0:
    print('NO')
else:
    for i in sequence:
        if i in '{[(':
            open_parentheses.append(i)
        elif not open_parentheses:  # if it is a closing parenthesis, do we have an opening parenthesis with which to connect the closing one?
            print('NO')
            break
        elif open_parentheses.pop() + i not in '{}[]()':
            print('NO')
            break
    else:
        print('YES')
