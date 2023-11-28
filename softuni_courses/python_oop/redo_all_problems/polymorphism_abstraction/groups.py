from abc import ABC


class Person(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

