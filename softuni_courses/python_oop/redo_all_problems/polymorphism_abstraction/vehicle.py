from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption ):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    INCREASE = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if (self.fuel_consumption + self.INCREASE) * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + self.INCREASE) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    INCREASE = 1.6
    LOSING_FUEL = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if (self.fuel_consumption + self.INCREASE) * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + self.INCREASE) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.LOSING_FUEL
