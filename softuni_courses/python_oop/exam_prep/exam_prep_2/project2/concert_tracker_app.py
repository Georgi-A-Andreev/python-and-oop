from project2.band import Band
from project2.band_members.drummer import Drummer
from project2.band_members.guitarist import Guitarist
from project2.band_members.musician import Musician
from project2.band_members.singer import Singer
from project2.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []

    def create_musician(self, musician_type, name, age):
        possible = ['Guitarist', 'Drummer', 'Singer']

        if musician_type not in possible:
            raise ValueError("Invalid musician type!")

        for i in self.musicians:
            if i.name == name:
                raise Exception(f"{name} is already a musician!")

        if musician_type == 'Guitarist':
            self.musicians.append(Guitarist(name, age))
        elif musician_type == 'Drummer':
            self.musicians.append(Drummer(name, age))
        else:
            self.musicians.append(Singer(name, age))

        return f"{name} is now a {musician_type}."

    def create_band(self, name):
        for i in self.bands:
            if i.name == name:
                raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))

        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        for i in self.concerts:
            if i.place == place:
                raise Exception(f"{place} is already registered for {i.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        if musician_name not in [i.name for i in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in [i.name for i in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        musician = [i for i in self.musicians if i.name == musician_name][0]
        band = [i for i in self.bands if i.name == band_name][0]

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        if band_name not in [i.name for i in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        band = [i for i in self.bands if i.name == band_name][0]

        if musician_name not in band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = [i for i in self.musicians if i.name == musician_name][0]

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        band = [i for i in self.bands if i.name == band_name][0]

        guitar = [i for i in band.members if type(i) == Guitarist]
        sing = [i for i in band.members if type(i) == Singer]
        drum = [i for i in band.members if type(i) == Drummer]

        if not all([guitar, sing, drum]):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [i for i in self.concerts if i.place == concert_place][0]
        valid = True
        if concert.genre == 'Rock':
            for i in band.members:
                if isinstance(i, Drummer):
                    if 'play the drums with drumsticks' not in i.skills:
                        valid = False

                if isinstance(i, Singer):
                    if 'sing high pitch notes' not in i.skills:
                        valid = False

                if isinstance(i, Guitarist):
                    if 'play rock' not in i.skills:
                        valid = False

        elif concert.genre == 'Metal':
            for i in band.members:
                if isinstance(i, Drummer):
                    if 'play the drums with drumsticks' not in i.skills:
                        valid = False

                if isinstance(i, Singer):
                    if 'sing low pitch notes' not in i.skills:
                        valid = False

                if isinstance(i, Guitarist):
                    if 'play metal' not in i.skills:
                        valid = False

        elif concert.genre == 'Jazz':
            for i in band.members:
                if isinstance(i, Drummer):
                    if 'play the drums with drum brushes' not in i.skills:
                        valid = False

                if isinstance(i, Singer):
                    if 'sing low pitch notes' not in i.skills or\
                            'sing high pitch notes' not in i.skills:
                        valid = False

                if isinstance(i, Guitarist):
                    if 'play jazz' not in i.skills:
                        valid = False

        if not valid:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

