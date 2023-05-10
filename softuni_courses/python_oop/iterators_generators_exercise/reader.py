def read_next(*args):

    for i in args:
        for j in i:
            yield j


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

