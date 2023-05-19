from project2.band_members.musician import Musician


class Singer(Musician):
    SKILLS = ['sing high pitch notes', 'sing low pitch notes']

    def __init__(self, name, age):
        super().__init__(name, age)

