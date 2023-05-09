class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence * number
        self.number = number
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == self.counter + 1:
            raise StopIteration

        self.counter += 1
        return self.sequence[self.counter]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')


