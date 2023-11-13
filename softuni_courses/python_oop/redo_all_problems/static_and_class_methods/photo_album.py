from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for idx, el in enumerate(self.photos):
            if len(el) < 4:
                el.append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(el)}"
        else:
            return f"No more free slots"

    def display(self):
        result = []
        result.append('-' * 11)
        for el in self.photos:
            if len(el) == 0:
                result.append('')
                result.append('-' * 11)
            else:
                result.append(' '.join(['[]' for _ in range(len(el))]))
                result.append('-' * 11)

        return '\n'.join(result)

