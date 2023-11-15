class Trainer:
    ID = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.generate_id() - 1

    @staticmethod
    def generate_id():
        Trainer.ID += 1
        return Trainer.ID

    @staticmethod
    def get_next_id():
        return Trainer.ID

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
