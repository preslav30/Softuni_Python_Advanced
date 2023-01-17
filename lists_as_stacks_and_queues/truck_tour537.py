from collections import deque

tank = 0
index = 0
pumps = int(input())
petrol_data = deque()
for pump in range(0, pumps):
    petrol_data.append(list(map(int, input().split())))
deque_copy = petrol_data.copy()

while deque_copy:
    gas, distance = deque_copy.popleft()
    tank += gas

    if tank < distance:
        petrol_data.append(petrol_data.popleft())
        deque_copy = petrol_data.copy()
        index += 1
        tank = 0
    else:
        tank -= distance

print(index)