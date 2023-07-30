import re

n = int(input())

pattern = r'(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'

for _ in range(n):
    password = input()

    match = re.findall(pattern, password)

    if not match:
        print('Try another password!')
        continue

    print(f'Password: {match[0][1] + match[0][2] + match[0][3] + match[0][4]}')

