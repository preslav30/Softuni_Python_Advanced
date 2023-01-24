r, c = list(map(int, input().split()))
matrix =[]


for row in range(r):
    for col in range(c):
        print(f"{chr(ord('a') + row)}{chr(col + row + ord('a'))}{chr(ord('a') + row)}", end=' ')
    print()
