text = input()
result = ''
for idx, el in enumerate(text):
    result += chr(ord(el) + 3)

print(result)