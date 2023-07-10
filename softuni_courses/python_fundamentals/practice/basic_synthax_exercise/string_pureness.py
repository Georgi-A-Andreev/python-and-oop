n = int(input())

for _ in range(n):
    text = input()

    if ',' not in text and '.' not in text and '_' not in text:
        print(f'{text} is pure.')
    else:
        print(f'{text} is not pure!')
