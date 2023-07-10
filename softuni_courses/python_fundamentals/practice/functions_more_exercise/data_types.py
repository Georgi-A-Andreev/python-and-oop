def data_type(type, content):
    if type == 'int':
        return int(content) * 2

    if type == 'real':
        return f'{float(content) * 1.5:.2f}'

    return f'${content}$'


type = input()
content = input()


print(data_type(type, content))
