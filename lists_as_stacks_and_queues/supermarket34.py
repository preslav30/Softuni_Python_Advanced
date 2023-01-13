from collections import deque

q = deque([])
while True:
    text = input()
    if text == 'End':
        print(f'{len(q)} people remaining.')
        break
    elif text == 'Paid':
        while q:
            print(q.popleft())
    else:
        q.append(text)

