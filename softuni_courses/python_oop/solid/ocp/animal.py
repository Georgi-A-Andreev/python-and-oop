from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Owl(Animal):
    def make_sound(self):
        return 'Hoof-Hoof'


def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())


animal_sounds([Cat(), Dog(), Owl()])
