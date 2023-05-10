import re

string = input()
pattern = r'\b(\d{2})+([\/.-])([A-Z][a-z]{2})+\2+(\d{4})\b'
result = re.findall(pattern, string)

for day, sep, month, year in result:
    print(f"Day: {day}, Month: {month}, Year: {year}")
