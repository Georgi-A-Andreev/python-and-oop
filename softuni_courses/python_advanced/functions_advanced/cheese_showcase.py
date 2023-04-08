def sorting_cheeses(**kwargs):
    result = []
    sorted_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for i, y in sorted_data:
        result.append(i)
        result.extend(sorted(y, reverse=True))

    return '\n'.join(str(x) for x in result)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
