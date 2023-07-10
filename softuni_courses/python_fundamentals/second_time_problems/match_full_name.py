import re

names = input()
regex = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"

match = re.findall(regex, names)

print(' '.join(match))
