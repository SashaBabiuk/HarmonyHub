from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
import pygame


Builder.load_file('style/musicplayerform.kv')

class MusicPlayerForm(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pygame.mixer.init()
        self.music_file = 'music/Foo Fighters - Everlong.mp3'
        self.album_art = 'images/everlong.jpg'
        self.slider_update_event = None
        self.track_length = 0
    def play_music(self):
        try:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
            self.track_length = pygame.mixer.Sound(self.music_file).get_length()
            self.ids.slider.max = self.track_length
            self.start_slider_update()
            self.update_album_art()
        except pygame.error as e:
            print(f"Error playing music: {e}")

    def pause_music(self):
        pygame.mixer.music.pause()
        self.stop_slider_update()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.stop_slider_update()
        self.ids.slider.value = 0
        self.ids.album_art.source = 'images/everlong.jpg'

    def start_slider_update(self):
        if self.slider_update_event is None:
            self.slider_update_event = Clock.schedule_interval(self.update_slider, 1.0 / 60.0)

    def stop_slider_update(self):
        if self.slider_update_event:
            self.slider_update_event.cancel()
            self.slider_update_event = None

    def update_slider(self, dt):
        if pygame.mixer.music.get_busy():
            self.ids.slider.value = pygame.mixer.music.get_pos() / 1000
        else:
            self.stop_slider_update()
            self.ids.slider.value = 0

    def update_album_art(self):
        self.ids.album_art.source = self.album_art

    def on_slider_touch_up(self, instance):
        if instance is self.ids.slider:
            pygame.mixer.music.play(start=instance.value)
            self.start_slider_update()


