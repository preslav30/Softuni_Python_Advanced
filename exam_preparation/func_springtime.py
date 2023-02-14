def start_spring(**kwargs):
    sorted_kwargs = {}
    for k, v in kwargs.items():
        if v not in sorted_kwargs.keys():
            sorted_kwargs[v] = []
        sorted_kwargs[v].append(k)
    for i, j in sorted_kwargs.items():
        j.sort()
    sorted_kwargs = dict(sorted(sorted_kwargs.items(), key=lambda x: (-len(x[1]), x[0])))
    result = []
    for x, y in sorted_kwargs.items():
        result.append(f'{x}:')
        for z in y:
            result.append(f'-{z}')
    return '\n'.join(result)

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
print()
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
print()
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

