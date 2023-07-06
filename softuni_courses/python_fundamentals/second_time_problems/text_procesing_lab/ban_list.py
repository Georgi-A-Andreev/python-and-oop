ban_words = input().split(', ')
text = input()

for word in ban_words:
    while word in text:
        text = text.replace(word, '*' * len(word))

print(text)