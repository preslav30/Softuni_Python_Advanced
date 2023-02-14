def shopping_cart(*meals):
    product_dict = {
        'Soup': [],
        'Pizza': [],
        'Dessert': [],
    }
    for meal in meals:
        if meal == 'Stop':
            break
        elif meal[1] not in product_dict[meal[0]] and len(product_dict[meal[0]]) < {"Soup": 3, "Pizza": 4, "Dessert": 2}[meal[0]]:
            product_dict[meal[0]].append(meal[1])
    for prod in product_dict.values():
        prod.sort()
    product_dict = dict(sorted(product_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    result = []
    all_empty = all(not v for v in product_dict.values())
    if all_empty:
        result = "No products in the cart!"
    else:
        for k, v in product_dict.items():
            result.append(f'{k}:')
            if v:
                for el in v:
                    result.append(f' - {el}')
        result = '\n'.join(result)

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

