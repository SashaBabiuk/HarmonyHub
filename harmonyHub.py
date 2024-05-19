from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from registrationForm import RegistrationForm
from loginForm import LoginForm
from mainForm import MainForm
from playlist1 import Playlist1
from playlist2 import Playlist2
from profileForm import ProfileForm
from musicPlayerForm import MusicPlayerForm


class HarmonyHub(MDApp):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(LoginForm(name='login'))
        sm.add_widget(RegistrationForm(name='registration'))
        sm.add_widget(MainForm(name='main'))
        sm.add_widget(Playlist1(name='playlist1'))
        sm.add_widget(Playlist2(name='playlist2'))
        sm.add_widget(ProfileForm(name='profile'))
        sm.add_widget(MusicPlayerForm(name='music'))
        return sm

    def switch_to_registration(self):
        self.root.current = 'registration'

    def switch_to_main(self):
        self.root.current = 'main'

    def switch_to_login(self):
        self.root.current = 'login'

    def play_playlist(self, namePlaylist):
        self.root.current = namePlaylist

    def on_back_button_pressed(self):
        self.root.current = 'main'

    def switch_screen(self, name):
        self.root.current = name

    def switch_to_profile(self):
        self.root.current = 'profile'

    def play_track(self):
        self.root.current = 'music'

