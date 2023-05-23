def my_f(a1):
    a2 = []
    for j in a1:
        a2.append(int(j))

    odd_sum = 0
    even_sum = 0
    for i in a2:
        if i % 2 == 0:
            even_sum += i
        elif i % 2 != 0:
            odd_sum += i
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


a = input()

x = my_f(a)
print(x)
