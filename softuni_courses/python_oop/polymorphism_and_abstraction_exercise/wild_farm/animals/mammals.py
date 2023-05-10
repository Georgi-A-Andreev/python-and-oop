from wild_farm.animals.animal import Mammal
from wild_farm.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if type(food) == Vegetable or type(food) == Fruit:
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.1
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if type(food) == Meat:
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.40
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if type(food) == Vegetable or type(food) == Meat:
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.30
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if type(food) == Meat:
            self.food_eaten += food.quantity
            self.weight += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
