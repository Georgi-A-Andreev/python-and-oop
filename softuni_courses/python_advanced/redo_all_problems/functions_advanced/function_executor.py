def func_executor(*args):
    result = []
    for el in args:
        result.append(f'{el[0].__name__} - {el[0](*el[1])}')

    return '\n'.join(result)

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

