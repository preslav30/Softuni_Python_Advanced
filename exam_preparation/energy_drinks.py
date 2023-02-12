from collections import deque

miligrams = list(map(int, input().split(', ')))
drinks = deque(map(int, input().split(', ')))
total_caffeine = 0
allowed_caffeine = 300
while drinks and miligrams:
    removed_ml = miligrams.pop()
    removed_drinks = drinks.popleft()
    caffeine_in_drink = removed_ml * removed_drinks
    if caffeine_in_drink + total_caffeine > 300:
        drinks.append(removed_drinks)
        if total_caffeine > 30:
            total_caffeine -= 30
        else:
            total_caffeine = 0
    else:
        total_caffeine += caffeine_in_drink


if drinks:
    print(f"Drinks left: {', '.join([str(x)for x in [*drinks]])}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")

