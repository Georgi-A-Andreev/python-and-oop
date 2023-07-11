import re

text = input().lower()
word = input().lower()

match = re.findall('\\b' + word + '\\b', text)

print(len(match))
