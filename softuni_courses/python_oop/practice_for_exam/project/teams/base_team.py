from abc import ABC, abstractmethod
from math import floor


class BaseTeam(ABC):
    def __init__(self, name, country, advantage, budget):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        return f"""Name: {self.name}
Country: {self.country}
Advantage: {self.advantage} points
Budget: {self.budget:.2f}EUR
Wins: {self.wins}
Total Equipment Price: {sum([a.price for a in self.equipment]):.2f}
Average Protection: {floor(sum([a.protection for a in self.equipment]) / len(self.equipment)) if self.equipment else 0}
"""
