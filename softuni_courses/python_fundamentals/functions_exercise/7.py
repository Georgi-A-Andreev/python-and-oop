def my_f(n1):
    result = []
    result.append(f'The minimum number is {min(n1)}')
    result.append(f'The maximum number is {max(n1)}')
    result.append(f'The sum number is: {sum(n1)}')
    return result


n = sorted([int(x) for x in input().split()])

x = my_f(n)

for i in range(len(x)):
    print(x[i])
