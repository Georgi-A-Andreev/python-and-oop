from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {'KneePad': KneePad, 'ElbowPad': ElbowPad}
    TEAM_TYPES = {'OutdoorTeam': OutdoorTeam, 'IndoorTeam': IndoorTeam}

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")
        self.equipment.append(self.EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type, team_name, country, advantage):
        if team_type not in self.TEAM_TYPES:
            raise Exception("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        self.teams.append(self.TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type, team_name):
        equipment = None
        for o in self.equipment[::-1]:
            if isinstance(o, self.EQUIPMENT_TYPES[equipment_type]):
                equipment = o
        team = None
        for t in self.teams:
            if t.name == team_name:
                team = t

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        team.budget -= equipment.price
        team.equipment.append(equipment)
        self.equipment.remove(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name):
        team = None
        for t in self.teams:
            if t.name == team_name:
                team = t
                break
        else:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f'The team has {team.wins} wins! Removal is impossible!')

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type):
        counter = 0
        for i in self.equipment:
            if isinstance(i, self.EQUIPMENT_TYPES[equipment_type]):
                i.increase_price()
                counter += 1
        return f'Successfully changed {counter}pcs of equipment.'

    def play(self, team_name1, team_name2):
        team1 = None
        team2 = None
        for i in self.teams:
            if i.name == team_name1:
                team1 = i
            if i.name == team_name2:
                team2 = i

        if type(team1) is not type(team2):
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points = team1.advantage + sum([i.protection for i in team1.equipment])
        team2_points = team2.advantage + sum([i.protection for i in team2.equipment])

        if team1_points == team2_points:
            return "No winner in this game."

        if team1_points > team2_points:
            team1.win()
            return f"The winner is {team_name1}."

        team2.win()
        return f"The winner is {team_name2}."

    def get_statistics(self):
        result = []
        result.append(f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:
""")
        for i in sorted(self.teams, key=lambda x: -x.wins):
            result.append(i.get_statistics())

        return ''.join(result)


t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())
