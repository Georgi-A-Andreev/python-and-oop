key = int(input())
symbols = int(input())
result = ''

for _ in range(symbols):
    symbol = input()
    char = ord(symbol) + key
    result += chr(char)

print(result)
