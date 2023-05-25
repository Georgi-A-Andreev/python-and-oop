n = int(input())
first = False

for i in range(n):
    a = input()
    if not first and a == ')':
        print('UNBALANCED')
        exit()

    if a == '(' and not first:
        first = True
        continue
    if first:
        if a == '(':
            print('UNBALANCED')
            exit()
    if first:
        if a == ')':
            first = False
        elif a == '(':
            print('UNBALANCED')
            exit()
print('BALANCED')
