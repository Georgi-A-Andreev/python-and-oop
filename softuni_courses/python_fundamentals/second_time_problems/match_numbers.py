import re

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

text = input()

result = re.finditer(pattern, text)

for match in result:
    print(match.group(), end=' ')
