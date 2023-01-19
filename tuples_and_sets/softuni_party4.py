n = int(input())

vip_= []
non_vip = []

codes = set()
for _ in range(n):
    codes.add(input())

while True:
    command = input()
    if command == 'END':
        break
    elif command in codes:
        codes.remove(command)

for code in codes:
    if code[0].isdigit():
        vip_.append(code)
    else:
        non_vip.append(code)
vip_.sort()
non_vip.sort()
print(len(vip_) + len(non_vip))
for x in vip_:
    print(x)
for y in non_vip:
    print(y)