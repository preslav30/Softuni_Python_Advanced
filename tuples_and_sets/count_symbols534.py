text = list(input())
counts = {}
for i in text:
    counts[i] = text.count(i)
counts = dict(sorted(counts.items()))
for  key, value in counts.items():
    print(f'{key}: {value} time/s')