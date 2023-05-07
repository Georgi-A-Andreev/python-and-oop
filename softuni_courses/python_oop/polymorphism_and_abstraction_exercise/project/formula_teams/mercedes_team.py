from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budged):
        super().__init__(budged)

    def calculate_revenue_after_race(self, race_pos):
        sponsors = 0
        if race_pos == 1:
            sponsors = 1000000 + 100000
        elif 1 < race_pos <= 3:
            sponsors = 500000 + 100000
        elif 3 < race_pos <= 5:
            sponsors = 100000
        elif 5 < race_pos <= 7:
            sponsors = 50000

        sponsors -= 200000
        self.budged += sponsors

        return f"The revenue after the race is {sponsors}$. Current budget {self.budged}$"
