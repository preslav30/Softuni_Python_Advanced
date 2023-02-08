def even_odd_filter(**kwargs):
    result = {'odd': [], 'even': []}
    for key, value in kwargs.items():
        if key == 'odd':
            for val in range(len(value)):
                if value[val] % 2 != 0:
                    result['odd'].append(value[val])
        elif key == 'even':
            for val in range(len(value)):
                if value[val] % 2 == 0:
                    result['even'].append(value[val])
    result = {key: value for key, value in result.items() if value}
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
