n = int(input())

for i in range(n):
    text = ''
    num = int(input())
    if num == 88:
        text = 'Hello'
    elif num == 86:
        text = 'How are you?'
    elif num > 88:
        text = 'Bye.'
    else:
        text = 'GREAT!'

    print(text)
