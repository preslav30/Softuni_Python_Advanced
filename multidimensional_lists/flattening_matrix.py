rows = int(input())

flattened = []

for row in range(rows):
    elements = list(map(int, input().split(', ')))
    for i in elements:
        flattened.append(i)
print(flattened)

