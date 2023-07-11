import re

pattern = r'\s([a-z0-9][a-z0-9\.\-\_]+@[a-z][a-z\-\.]+[\.][a-z]+)\b'

text = input()
result = re.findall(pattern, text)
print(*result, sep='\n')
