lines = int(input())
my_list = []

for _ in range(lines):
    text = input()

    if text not in ('(', ')'):
        continue

    if text == '(':
        my_list.append(text)

    if len(my_list) == 1 and text == ')':
        my_list.pop()

    elif len(my_list) == 0 and text == ')':
        my_list.append(text)
        break


if len(my_list):
    print('UNBALANCED')
else:
    print('BALANCED')


