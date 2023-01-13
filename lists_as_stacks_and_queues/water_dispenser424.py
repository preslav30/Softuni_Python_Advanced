from collections import deque

names_q = deque()
starting_quantity = int(input())
while True:
    names = input()
    if names == 'Start':
        break
    names_q.append(names)

while True:
    command = input()
    if command == 'End':
        print(f'{starting_quantity} liters left')
        break
    elif command.isnumeric():
        liters = int(command)
        if starting_quantity >= liters:
            print(f'{names_q.popleft()} got water')
            starting_quantity -= liters
        else:
            print(f'{names_q.popleft()} must wait')
    elif command.split()[0] == 'refill':
        starting_quantity += int(command.split()[1])


