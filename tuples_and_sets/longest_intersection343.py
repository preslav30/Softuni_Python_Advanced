n = int(input())


longest = {}
for i in range(n):
    nums = set()
    starts = set()
    ends = set()
    f, s = input().split('-')
    first_start, first_end = f.split(',')
    second_start, second_end = s.split(',')
    first_start, first_end, second_start, second_end = int(first_start), int(first_end), int(second_start), int(second_end)
    for x in range(first_start, first_end + 1):
        starts.add(x)
    for y in range(second_start, second_end + 1):
        ends.add(y)
    if len(starts & ends) > len(longest):
        longest = starts & ends

print(f"Longest intersection is [{', '.join(map(str, longest))}] with length {len(longest)}")