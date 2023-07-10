level_of_fire = input().split('#')
water = int(input())

effort = 0
total_fire = 0
print('Cells:')
for i in level_of_fire:
    fire_type, value = i.split(' = ')
    value = int(value)

    if fire_type == 'High' and 81 <= value <= 125:
        pass

    elif fire_type == 'Medium' and 51 <= value <= 80:
        pass

    elif fire_type == 'Low' and 1 <= value <= 50:
        pass

    else:
        continue

    if water - value < 0:
        continue

    water -= value
    effort += value * 0.25
    total_fire += value

    print(f' - {value}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
