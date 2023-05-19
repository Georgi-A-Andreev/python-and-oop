from abc import ABC, abstractmethod


class Delicacy(ABC):

    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError('Name cannot be null or whitespace!')
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be less or equal to zero!")
        else:
            self.__price = value

    @abstractmethod
    def details(self):
        pass

