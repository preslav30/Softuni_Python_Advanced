lists = input().split('|')
listss = []

for i in lists[::-1]:
    listss.extend(i.split())
print(*listss)