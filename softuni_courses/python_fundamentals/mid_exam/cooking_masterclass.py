from math import ceil

budged = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

total_flour = price_flour * (students - students // 5)
total_eggs = students * 10 * price_egg
total_aprons = ceil(students * 1.2) * price_apron

total_price = total_aprons + total_eggs + total_flour

if total_price <= budged:
    print(f'Items purchased for {total_price:.2f}$.')
else:
    print(f'{total_price - budged:.2f}$ more needed.')
