n = int(input())

for i in range(n):
    x = int(input())
    if x % 2 == 1:
        print(f'{x} is odd!')
        break
else:
    print('All numbers are even.')
