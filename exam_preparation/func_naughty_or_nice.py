def naughty_or_nice_list(names, *args, **kwargs):
    sorted_kids = {}
    kid_qualities = {
        'Nice': [],
        'Naughty': [],
        'Not found': [],
    }
    for number, kid in names:
        if number not in sorted_kids.keys():
            sorted_kids[number] = []
        sorted_kids[number].append(kid)
    for arg in args:
        num, quality = arg.split('-')
        num = int(num)
        if num in sorted_kids.keys():
            if len(sorted_kids[num]) == 1:
                kid_qualities[quality].append(sorted_kids[num][0])
                sorted_kids.pop(num)
    for k, v in kwargs.items():
        count = 0
        for lst in sorted_kids.values():
            count += lst.count(k)
        if count == 1:
            for a, b in sorted_kids.items():
                for n in b:
                    if n == k:
                        sorted_kids[a].remove(k)
                        kid_qualities[v].append(k)
    for s, l in sorted_kids.items():
        if l:
            kid_qualities['Not found'].append(l[0])
    result = []
    for k, v in kid_qualities.items():
        if v:
            result.append(f"{k}: {', '.join([str(x) for x in [*v]])}")
    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
print()
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
