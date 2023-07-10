line = [int(i) for i in input().split(', ')]

positive = []
negative = []
even = []
odd = []

[positive.append(i) if i >= 0 else negative.append(i) for i in line]
[even.append(i) if i % 2 == 0 else odd.append(i) for i in line]
print(f'''
Positive: {', '.join(str(x) for x in positive)}
Negative: {', '.join(str(x) for x in negative)}
Even: {', '.join(str(x) for x in even)}
Odd: {', '.join(str(x) for x in odd)} 
''')
