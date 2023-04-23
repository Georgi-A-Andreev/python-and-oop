from softuni_courses.python_oop.classes_and_objects_exercise.project3.album import Album
from softuni_courses.python_oop.classes_and_objects_exercise.project3.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for a in self.albums:
            if a.name == album_name and a.published:
                return "Album has been published. It cannot be removed."
            if a.name == album_name and not a.published:
                self.albums.remove(a)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n" + '\n'.join([a.details() for a in self.albums])


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
