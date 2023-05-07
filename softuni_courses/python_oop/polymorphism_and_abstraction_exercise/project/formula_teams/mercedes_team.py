from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos):
        sponsors = 0
        if race_pos == 1:
            sponsors = 1_000_000 + 100_000
        elif 1 < race_pos <= 3:
            sponsors = 500_000 + 100_000
        elif 3 < race_pos <= 5:
            sponsors = 100_000
        elif 5 < race_pos <= 7:
            sponsors = 50_000

        result = sponsors - 200_000
        self.budged += result
        return f"The revenue after thе race is {result}$. Current budget {self.budged}$"
