text = input()
print(text[0], end='')
for idx, el in enumerate(text):
    if idx > 0 and text[idx] != text[idx - 1]:
        print(el, end='')