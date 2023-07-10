text = input()
result = []

for i in range(len(text)):
    if text[i].isupper():
        result.append(i)

print(result)
