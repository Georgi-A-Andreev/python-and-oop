class ExercisePlan:
    ID = 1
    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.generate_id() - 1

    @staticmethod
    def generate_id():
        ExercisePlan.ID += 1
        return ExercisePlan.ID

    @staticmethod
    def get_next_id():
        return ExercisePlan.ID

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours * 60)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
