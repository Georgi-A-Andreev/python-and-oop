def grocery_store(**kwargs):
    result = []

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for k, v in kwargs:
        result.append(f'{k}: {v}')

    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
