import re

dates = input()

regex = r'(\b[0-9]{2})(\.|\-|\/)([A-Z][a-z]{2})\2([0-9]{4}\b)'
match = re.findall(regex, dates)

for day, sep, month, year in match:
    print(f"Day: {day}, Month: {month}, Year: {year}")
