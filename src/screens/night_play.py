from pygame import Surface

from src.screens.office_screen import OfficeScreen
from src.screens.cameras_screen import CamerasScreen
from src.event_handler import EventHandler



class NightPlay(object):
    def __init__(
            self,
            WIDTH: int,
            HEIGHT: int,
            main_screen: Surface
    ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.main_screen = main_screen
        self.night_screen = "office"
        self.office = OfficeScreen(self.WIDTH, self.HEIGHT, self.main_screen)
        self.cameras = CamerasScreen(self.WIDTH, self.HEIGHT, self.main_screen)

    def night_screen_switcher(self, event_wait: EventHandler):
        if self.night_screen == "office":
            night_screen = self.office.office_screen(event_wait)
            if night_screen != None:
                self.night_screen = night_screen

        elif self.night_screen == "cameras":
            night_screen = self.cameras.cameras_screen(event_wait)
            if night_screen != None:
                self.night_screen = night_screen
