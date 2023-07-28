import re

emoji_pattern = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})\1'
number_pattern = r'\d'

text = input()

match_numbers = re.findall(number_pattern, text)

cool_factor = 1
for num in match_numbers:
    cool_factor *= int(num)

emoji_match = re.findall(emoji_pattern, text)

print(f'Cool threshold: {cool_factor}')
print(f"{len(emoji_match)} emojis found in the text. The cool ones are:")
for el in emoji_match:
    symbols = el[0]
    emoji = el[1]
    score = 0
    for char in emoji:
        score += ord(char)

    if score >= cool_factor:
        print(symbols + emoji + symbols)
