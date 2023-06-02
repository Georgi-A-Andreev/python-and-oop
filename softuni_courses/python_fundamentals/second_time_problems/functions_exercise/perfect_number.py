def verify_perfect_number(number):
    summ = 0
    for i in range(1, number):
        if number % i == 0:
            summ += i

    if summ == number:
        return f'We have a perfect number!'

    return "It's not so perfect. "


n = int(input())

print(verify_perfect_number(n))