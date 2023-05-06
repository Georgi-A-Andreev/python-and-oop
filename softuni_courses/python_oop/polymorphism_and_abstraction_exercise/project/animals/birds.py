
from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if type(food) == Meat:
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.25
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35
