from collections import deque

tank = 0
index = 0
pumps = int(input())
petrol_data = deque()
for pump in range(0, pumps):
    petrol_data.append(list(map(int, input().split())))
deque_copy = petrol_data.copy()

while deque_copy:
    '''pop the first element of the copy so that if the correct condition is fulfilled, it will keep popping
    until the list is empty. Otherwise the copied list will be renewed to be like the full, modified original list'''
    gas, distance = deque_copy.popleft()
    tank += gas

    if tank < distance:
        petrol_data.append(petrol_data.popleft())
        deque_copy = petrol_data.copy()  # reset the copied list to be like the modified original list so we can then pop the new rotated value
        index += 1
        tank = 0
    else:
        tank -= distance

print(index)