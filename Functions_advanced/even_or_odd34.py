def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    operations = {
        'even': [i for i in numbers if i % 2 == 0],
        'odd': [i for i in numbers if i % 2 != 0]
    }

    return operations[command]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

