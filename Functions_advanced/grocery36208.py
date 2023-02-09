def grocery_store(**kwargs):  # {'bread': 5, 'pasta': 12, 'eggs': 12}
    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    output = ''
    for i in sorted_items:
        output += f'{i[0]}: {i[1]}\n'
    return output


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
