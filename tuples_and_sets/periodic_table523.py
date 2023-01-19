n = int(input())

unique = set()
for _ in range(n):
    lst = input().split()
    for j in lst:
        unique.add(j)


for i in unique:
    print(i)