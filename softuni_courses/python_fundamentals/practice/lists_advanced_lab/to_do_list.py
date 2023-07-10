notes = {}
result = []

while True:
    note = input()

    if note == 'End':
        break

    note = note.split('-')
    notes[int(note[0])] = note[1]


for k, v in sorted(notes.items()):
    result.append(v)

print(result)
