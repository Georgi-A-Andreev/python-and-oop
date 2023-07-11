import re
result = 0
bought = []
pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)'

while True:
    text = input()
    if text == 'Purchase':
        break
    match = re.match(pattern, text)
    if match:
        name, price, quantity = match.groups()

        bought.append(name)
        result += int(quantity) * float(price)
#
# print('Bought furniture:')
# print(*bought, sep='\n')
# print(f'Total money spend: {result:.2f}')

print('Bought furniture:')
for i in bought:
    print(i)
print(f'Total money spend: {result:.2f}')
