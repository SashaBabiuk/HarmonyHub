from kivymd.uix.screen import Screen
from kivy.lang import Builder


# Завантаження файлу стилів
Builder.load_file('style/playlist1.kv')


class Playlist1(Screen):
    playlist_name = "My Playlist"

    def __init__(self, playlist_name='', **kwargs):
        super(Playlist1, self).__init__(**kwargs)
        self.playlist_name = playlist_name