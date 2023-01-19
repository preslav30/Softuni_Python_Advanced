n, m = list(map(int, input().split()))

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(int(input()))

for _ in range(m):
    m_set.add(int(input()))
unique = set(n_set & m_set)
for i in unique:
    print(i)