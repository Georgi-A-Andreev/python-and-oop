import re
words = []
match_words = []

text = input()

pattern = r'(@|\#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'

match = re.findall(pattern, text)
for el in match:
    first = el[1]
    second = el[2][::-1]
    if first == second:
        match_words.append(f'{first} <=> {second[::-1]}')
        words.append(first)
    else:
        words.append(first)

if len(words) == 0:
    print("No word pairs found!")
else:
    print(f"{len(words)} word pairs found!")

if len(match_words) == 0:
    print("No mirror words!")
else:
    print('The mirror words are:')
    print(', '.join(match_words))
