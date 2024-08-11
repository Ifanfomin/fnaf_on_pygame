from src.scripts.base_funcs import load_images, view_image
from pygame import mixer as Mixer
from pygame import event as Event
from pygame import Surface
from src.scripts.event_handler import EventHandler
from time import time


class TitleScreen(object):
    def __init__(
            self,
            WIDTH: int,
            HEIGHT: int,
            screen: Surface
    ):
        self.main_screen = screen
        self.frm_number = 1
        self.frm_switch = False
        self.frm_time = 0
        self.frames = load_images("src/media/images/title_screen_images", WIDTH, HEIGHT)
        Mixer.music.load("src/media/sounds/title_screen_music_sin_nanna.mp3")
        Mixer.music.play()

    def title_screen(
            self,
            event_wait: EventHandler
    ):
        if self.frm_switch == False:
            self.frm_time = time()
            self.frm_switch = True
        if time() - self.frm_time > 0.03:
            self.frm_switch = False
            if self.frm_number == 5:
                self.frm_number = 1
            else:
                self.frm_number += 1

        view_image(self.frames[f"title_{str(self.frm_number)}.png"], self.main_screen)

        scene = event_wait.title_screen_handler(Event.get())
        return scene
