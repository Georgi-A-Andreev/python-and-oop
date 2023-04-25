class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        if self.data:
            x = self.data[-1]
            return x

    def is_empty(self):
        return not bool(self.data)

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"
