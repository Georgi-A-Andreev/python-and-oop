from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    EXTRA_FUEL = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if distance * (self.fuel_consumption + Car.EXTRA_FUEL) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + Car.EXTRA_FUEL)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    EXTRA_FUEL = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if distance * (self.fuel_consumption + Truck.EXTRA_FUEL) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + Truck.EXTRA_FUEL)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
