text = input()
for idx, char in enumerate(text):
    if char == ':':
        print(text[idx:idx + 2])

