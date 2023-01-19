nums = tuple(map(float, input().split()))
nums_and_occurrences = {}
for num in nums:
    if num not in nums_and_occurrences:
        nums_and_occurrences[num] = nums.count(num)

for num, occ in nums_and_occurrences.items():
    print(f"{num} - {occ} times")
