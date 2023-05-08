import re

text = input()
pattern = fr'\b{input()}\b'
result = re.findall(pattern, text, re.IGNORECASE)
print(len(result))
