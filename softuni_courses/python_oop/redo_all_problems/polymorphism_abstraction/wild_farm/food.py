from abc import ABC


class Food(ABC):
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Seed (Food):
    def __init__(self, quantity):
        super().__init__(quantity)
