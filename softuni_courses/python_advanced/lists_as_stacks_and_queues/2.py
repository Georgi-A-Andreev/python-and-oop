text = input()
result = []
counter = -1
last_word_index = []
for i in text:
    counter += 1
    if i == '(':
        last_word_index.append(counter)
        result.append(i)
    if i == ')':
        print(text[last_word_index[-1]:counter + 1])
        result.pop()
        last_word_index.pop()
