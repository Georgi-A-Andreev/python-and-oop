from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)
        self.guests += room.guests

    def take_room(self, room_number, people):
        for r in self.rooms:
            if r.number == room_number:
                if not r.take_room(people):
                    self.guests += people

    def free_room(self, room_number):
        for i in self.rooms:
            if i.number == room_number:
                x = i.guests
                if not i.free_room():
                    self.guests -= x

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" + \
            f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n" + \
            f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}\n"

