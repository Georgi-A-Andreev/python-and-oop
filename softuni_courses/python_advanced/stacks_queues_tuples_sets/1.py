first = set()
seconds = set()

[first.add(int(i)) for i in input().split()]
[seconds.add(int(i)) for i in input().split()]

commands = {
    'Add First': lambda x: [first.add(int(i)) for i in x],
    'Add Second': lambda x: [seconds.add(int(i)) for i in x],
    'Remove First': lambda x: [first.discard(int(i)) for i in x],
    'Remove Second': lambda x: [seconds.discard(int(i)) for i in x],
    'Check Subset': lambda: print(first.issubset(seconds) or seconds.issubset(first)),
}

for i in range(int(input())):
    command, *other = input().split()
    commands[f'{command} {other[0]}'](other[1:]) if len(other) > 1 else commands[f'{command} {other[0]}']()

print(*sorted(first), sep=', ')
print(*sorted(seconds), sep=', ')
