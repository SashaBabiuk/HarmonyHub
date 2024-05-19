from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('style/playlist2.kv')

class Playlist2(Screen):
    playlist_name = "My Playlist 2"

    def __init__(self, playlist_name='', **kwargs):
        super(Playlist2, self).__init__(**kwargs)
        self.playlist_name = playlist_name

