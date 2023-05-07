from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budged):
        super().__init__(budged)

    def calculate_revenue_after_race(self, race_pos):
        sponsors = 0
        if race_pos == 1:
            sponsors = 1500000 + 20000
        elif race_pos == 2:
            sponsors = 800000 + 20000
        elif 2 < race_pos <= 8:
            sponsors = 20000
        elif 8 < race_pos <= 10:
            sponsors = 10000

        sponsors -= 250000
        self.budged += sponsors

        return f"The revenue after the race is {sponsors}$. Current budget {self.budged}$"
