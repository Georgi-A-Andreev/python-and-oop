import re

n = int(input())

pattern = r'(.)(\1{0,})>([0-9]+)\|([a-z]+)\|([A-Z]+)\|([^<>]+)<\1\2$'

for _ in range(n):
    password = input()

    match = re.findall(pattern, password)

    if not match:
        print('Try another password!')
        continue

    print(f'Password: {match[0][2] + match[0][3] + match[0][4] + match[0][5]}')

