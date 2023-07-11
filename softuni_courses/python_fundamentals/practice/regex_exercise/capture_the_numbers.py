import re


regex = r'\d+'
text = input()
while text:
    if not re.findall(regex, text):
        text = input()
        continue
    print(*re.findall(regex, text), end=' ')

    text = input()