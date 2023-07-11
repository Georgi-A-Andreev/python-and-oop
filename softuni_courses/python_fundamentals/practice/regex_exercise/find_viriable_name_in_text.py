import re

regex = r'\b_([A-Za-z0-9]+\b)'
text = input()

match = re.findall(regex, text)

print(*match, sep=',')