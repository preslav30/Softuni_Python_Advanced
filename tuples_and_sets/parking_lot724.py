n = int(input())

cars = {}
empty = True
for _ in range(n):
    direction, car_number = input().split(', ')
    cars[car_number] = direction
for car, direction in cars.items():
    if direction == 'IN':
        empty = False
        print(car)
if empty:
    print('Parking Lot is Empty')