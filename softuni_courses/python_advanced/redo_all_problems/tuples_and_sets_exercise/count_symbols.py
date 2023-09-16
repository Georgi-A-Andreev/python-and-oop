text = input()

chars = {}

for char in text:
    if char not in chars:
        chars[char] = 0
    chars[char] += 1

for k, v in sorted(chars.items()):
    print(f'{k}: {v} time/s')