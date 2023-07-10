import re

phones = input()
regex = r'\+359-2-[0-9]{3}-[0-9]{4}\b|\+359 2 [0-9]{3} [0-9]{4}\b'
match = re.findall(regex, phones)

print(', '.join(match))
