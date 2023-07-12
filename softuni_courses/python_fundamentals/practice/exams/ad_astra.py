import re

text = input()
total_calories = 0
pattern = r'(#|\|)([a-z A-Z]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1'

match = re.findall(pattern, text)

for i in match:
    total_calories += int(i[-1])

total_days = total_calories // 2000

print(f'You have food to last you for: {total_days} days!')
for i in match:
    print(f"Item: {i[1]}, Best before: {i[2]}, Nutrition: {i[3]}")
