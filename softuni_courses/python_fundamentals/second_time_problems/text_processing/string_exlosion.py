text = input().split('>')

for idx, el in enumerate(text):
    if el[0].isdigit():
        power = int(el[0])
        text[idx] = el[min(power, len(el)):].strip()

print('>'.join(text))
