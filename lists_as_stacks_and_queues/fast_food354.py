from collections import deque

quantity_for_the_day = int(input())
food_in_each_order = deque(map(int, input().split()))
print(max(food_in_each_order))
while food_in_each_order:
    if quantity_for_the_day - food_in_each_order[0] >= 0:

        quantity_for_the_day -= food_in_each_order[0]
        food_in_each_order.popleft()

    else:
        print(f"Orders left: ", end='')
        print(*food_in_each_order, sep=' ')
        quit()
print("Orders complete")