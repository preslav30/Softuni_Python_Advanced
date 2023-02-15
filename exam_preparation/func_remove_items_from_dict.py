def shopping_list(budget, **kwargs):
    basket = 0
    basket_full = False
    result = []
    if budget < 100:
        return "You do not have enough budget."

    while kwargs:
        for prod, price in list(kwargs.items()):
            if basket == 5:
                basket_full = True
                break
            total_price = price[0] * price[1]
            if total_price <= budget:
                basket += 1
                budget -= total_price
                result.append(f"You bought {prod} for {total_price:.2f} leva.")
            kwargs.pop(prod)
        if basket_full:
            break
    return '\n'.join(result)

# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# print()
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

