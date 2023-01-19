
odd = set()
even = set()
for row in range(1, int(input()) + 1):
    name = input()
    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)
    result = ascii_sum // row
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)

if sum(odd) == sum(even):
    print(*odd.union(even), sep=', ')

elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=', ')
else:
    print(*odd.symmetric_difference(even), sep=', ')
