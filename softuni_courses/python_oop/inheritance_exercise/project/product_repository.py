from project.food import Food
from project.drink import Drink


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for i in self.products:
            if i.name == product_name:
                return i

    def remove(self, product_name):
        for i in self.products:
            if i.name == product_name:
                self.products.remove(i)
                break

    def __repr__(self):
        return '\n'.join(f"{i.name}: {i.quantity}" for i in self.products)


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
