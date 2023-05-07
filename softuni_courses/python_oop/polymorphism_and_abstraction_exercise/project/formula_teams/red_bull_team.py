from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos):
        sponsors = 0
        if race_pos == 1:
            sponsors = 1_500_000 + 20_000
        elif race_pos == 2:
            sponsors = 800_000 + 20_000
        elif 3 <= race_pos <= 8:
            sponsors = 20_000
        elif 8 < race_pos <= 10:
            sponsors = 10_000

        result = sponsors - 250_000
        self.budged += result
        return f"The revenue after thе race is {result}$. Current budget {self.budged}$"
