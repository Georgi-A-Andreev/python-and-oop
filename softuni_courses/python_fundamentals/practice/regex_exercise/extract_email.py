import re

text = input()
regex = r'\s([a-z0-9][a-z0-9\.\-\_]+@[a-z][a-z\-\.]+[\.][a-z]+)\b'
match = re.findall(regex, text)

print(*match, sep='\n')
