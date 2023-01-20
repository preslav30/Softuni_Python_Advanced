from collections import deque

materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))
presents_crafted = dict()
toys = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400,
}
task_complete = False

while materials and magic_level:
    box = materials[-1]
    magic = magic_level[0]
    total_magic_level = box * magic
    if total_magic_level in toys.values():
        materials.pop()
        magic_level.popleft()
        toy = ''.join([name for name, level in toys.items() if level == total_magic_level])
        if toy in presents_crafted.keys():
            presents_crafted[toy] += 1
        else:
            presents_crafted[toy] = 1
    elif total_magic_level < 0:
        total_magic_level = box + magic
        materials.pop()
        magic_level.popleft()
        materials.append(total_magic_level)
    elif total_magic_level > 0 and total_magic_level not in toys.values():
        magic_level.popleft()
        materials[-1] += 15
    if box == 0:
        materials.pop()
    if magic == 0:
        magic_level.popleft()

if 'Doll' in presents_crafted.keys() and 'Wooden train' in presents_crafted.keys():
    task_complete = True
if 'Teddy bear' in presents_crafted.keys() and 'Bicycle' in presents_crafted.keys():
    task_complete = True

if task_complete:
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')

if materials:
    print(f'Materials left: ', end='')
    for x in range(len(materials) - 1, 0, -1):
        print(materials[x], end=', ')
    print(materials[0])
if magic_level:
    print(f'Magic left: ', end='')
    print(*magic_level, sep=', ')
presents_crafted = dict(sorted(presents_crafted.items()))

for key, value in presents_crafted.items():
    print(f'{key}: {value}')

