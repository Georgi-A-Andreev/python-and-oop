import re
pattern = r'\d+'
text = input()
while text:

    result = re.findall(pattern, text)
    for i in result:
        print(i, end=' ')
    text = input()
