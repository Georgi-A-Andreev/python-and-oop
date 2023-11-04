from project.song import Song

class Album:
    def __init__(self, name, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = []

    def add_song(self, song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        for s in self.songs:
            if s.name == song_name:
                if self.published:
                    return "Cannot remove songs. Album is published."
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = []
        result.append(f'Album {self.name}')
        for s in self.songs:
            result.append(f' == {s.get_info()}')

        return '\n'.join(result)
