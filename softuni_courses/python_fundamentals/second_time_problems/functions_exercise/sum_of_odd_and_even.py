def sum_of_odd_and_even(num):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for el in str(num):
        el = int(el)

        if el % 2 == 0:
            sum_of_even_digits += el
        else:
            sum_of_odd_digits += el

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


input_number = int(input())

print(sum_of_odd_and_even(input_number))