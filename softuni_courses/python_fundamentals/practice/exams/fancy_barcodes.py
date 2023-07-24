import re

pattern = r'@{1}#+[A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1}@{1}#+'

n = int(input())

for _ in range(n):
    code = input()
    match = re.findall(pattern, code)

    if not match:
        print('Invalid barcode')
        continue

    group = ''
    for char in match[0]:
        if char.isdigit():
            group += char

    if group == '':
        print('Product group: 00')
    else:
        print(f'Product group: {group}')