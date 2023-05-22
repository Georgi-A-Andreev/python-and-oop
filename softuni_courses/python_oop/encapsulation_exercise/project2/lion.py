from project2.animal import Animal


class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int, money_for_care: int = 50):
        super().__init__(name, gender, age, money_for_care)
