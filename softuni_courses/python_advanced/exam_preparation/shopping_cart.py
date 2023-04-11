def shopping_cart(*args):
    in_shopping_list = False
    shopping_list = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for i in args:
        if i == 'Stop':
            break

        if (i[0] == 'Soup' and len(shopping_list[i[0]]) < 3) or \
                (i[0] == 'Pizza' and len(shopping_list[i[0]]) < 4) or \
                (i[0] == 'Dessert' and len(shopping_list[i[0]]) < 2):
            if i[1] not in shopping_list[i[0]]:
                shopping_list[i[0]].append(i[1])
                in_shopping_list = True
    if not in_shopping_list:
        return 'No products in the cart!'

    sorted_shopping_list = dict(sorted(shopping_list.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''
    for meal, product in sorted_shopping_list.items():
        result += f'{meal}:\n'
        for p in sorted(product):
            result += f' - {p}\n'

    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
