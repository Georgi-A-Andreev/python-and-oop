rol, col = [int(x) for x in input().split()]

text = input()
new_text = text * rol * col
counter = 0
for r in range(1, rol+1):
    for c in range(col):
        if r % 2 != 0:
            print(new_text[counter], end='')
            counter += 1
        else:
            for i in range(r*col, r*col-col, -1):
                print(new_text[i-1], end='')
            counter += col
            break
    print()
