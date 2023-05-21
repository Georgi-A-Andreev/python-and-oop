from project2.band_members.musician import Musician


class Guitarist(Musician):
    SKILLS = ['play metal',
              'play rock',
              'play jazz']

    def __init__(self, name, age):
        super().__init__(name, age)
