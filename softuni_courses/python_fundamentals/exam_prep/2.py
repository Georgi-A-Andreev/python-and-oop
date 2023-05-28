import re
result = []
total_result = []
mirror_words = []
text_string = input()
pattern = r'([\#|\@])([a-zA-Z]{3,}\1{2}[a-zA-Z]{3,})\1'
result2 = re.findall(pattern, text_string)

for i in result2:
    result.append(i[1])

if len(result) > 0:
    print(f'{len(result)} word pairs found!')
else:
    print('No word pairs found!')
for i in result:
    if '@' in i:
        i = i.split('@@')
    else:
        i = i.split('##')
    total_result.append(i)
for i in total_result:
    if i[0] == i[1][::-1]:
        mirror_words.append(i[0])
counter = 0
if len(mirror_words) > 0:
    print('The mirror words are:')
    for i in mirror_words:
        counter += 1
        if counter == len(mirror_words):
            print(f'{i} <=> {i[::-1]}')
        else:
            print(f'{i} <=> {i[::-1]}', end=', ')
else:
    print('No mirror words!')
