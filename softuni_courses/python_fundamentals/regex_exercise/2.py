import re

patten = r'\b[_]([a-zA-Z0-9]+)\b'

text = input()
result = re.findall(patten, text)
print(','.join(result))
