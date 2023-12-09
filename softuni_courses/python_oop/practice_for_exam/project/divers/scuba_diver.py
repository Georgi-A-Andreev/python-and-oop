from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 540)

    def miss(self, time_to_catch):
        self.oxygen_level = max(self.oxygen_level - round(time_to_catch * 0.3), 0)

    def renew_oxy(self):
        self.oxygen_level = 540