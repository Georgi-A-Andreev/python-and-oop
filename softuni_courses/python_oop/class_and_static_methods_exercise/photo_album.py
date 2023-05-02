from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for r in range(len(self.photos)):
            if len(self.photos[r]) < 4:
                self.photos[r].append(label)
                return f"{label} photo added successfully on page {r + 1} slot {self.photos[r].index(label) + 1}"
        return "No more free slots"

    def display(self):
        result = f"{'-' * 11}\n"
        for i in self.photos:
            result += f"{('[] ' * len(i)).rstrip()}\n" + f"{'-' * 11}\n"

        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
