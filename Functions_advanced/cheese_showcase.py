def sorting_cheeses(**cheeses):
    sorted_cheeses = dict(sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0])))  # {'Camembert': [100, 100, 105, 500, 430], 'Parmesan': [102, 120, 135], 'Mozzarella': [50, 125]}
    for key in sorted_cheeses:
        sorted_cheeses[key] = sorted(sorted_cheeses[key], reverse=True)

    return "\n".join([key + "\n" + "\n".join(map(str, v)) for key, v in sorted_cheeses.items()])



print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)


