from src.scripts.base_funcs import load_images, view_image
from pygame import mixer as Mixer
from pygame import event as Event
from pygame import Surface
from time import time

from src.scripts.event_handler import EventHandler


class OfficeScreen(object):
    def __init__(
            self,
            WIDTH: int,
            HEIGHT: int,
            main_screen: Surface
    ):
        self.main_screen = main_screen
        self.frm_number = 1
        self.frm_switch = False
        self.frm_time = 0
        self.image = "pc"
        self.new_pos = 2  # части офиса слева направо от 1 до 3
        self.old_pos = 2
        self.light = "light"
        self.doors = ["left_4_open", "right_4_open"]
        self.light_on_off_sounds = [
            Mixer.Sound("src/media/sounds/light_on_sound.wav"),
            Mixer.Sound("src/media/sounds/light_off_sound.wav")
        ]
        self.frames = load_images("src/media/images/office_screen_images/night_office", WIDTH, HEIGHT)

    def office_screen(
            self,
            event_wait: EventHandler
    ):
        # print("Старая позиция: " + str(self.old_pos), "Новая позиция: " + str(self.new_pos))
        image = self.pos_handler()
        if image != None:
            self.image = image

        view_image(self.frames[f"{str(self.image)}_{self.light}.png"], self.main_screen)

        return self.action_handler(event_wait)

    def action_handler(
            self,
            event_wait: EventHandler
    ):
        action = event_wait.office_screen_handler(Event.get())
        if action == "right" and self.new_pos != 3 and (self.new_pos - self.old_pos != -1):
            print(action)
            self.new_pos += 1
        elif action == "left" and self.new_pos != 1 and (self.new_pos - self.old_pos != 1):
            print(action)
            self.new_pos -= 1

        elif action == "right_switched" and self.old_pos == self.new_pos == 3:
            if self.image == "right_4_open":
                self.doors[1] = "right_4_close"
                self.image = "right_4_close"
            else:
                self.doors[1] = "right_4_open"
                self.image = "right_4_open"

        elif action == "left_switched" and self.old_pos == self.new_pos == 1:
            if self.image == "left_4_open":
                self.doors[0] = "left_4_close"
                self.image = "left_4_close"
            else:
                self.doors[0] = "left_4_open"
                self.image = "left_4_open"

        elif action == "light_switched":
            if self.light == "light":
                self.light = "dark"
                self.light_on_off_sounds[1].play()
            else:
                self.light = "light"
                self.light_on_off_sounds[0].play()

        elif action == "pc_open" and self.new_pos == self.old_pos == 2:  # проверка на открытие камер и нахождения у пк
            return "cameras"

    def pos_handler(self):
        if self.old_pos == 1 and self.new_pos == 3 or self.old_pos == 3 and self.new_pos == 1:
            self.new_pos = 2
        elif self.old_pos == 2 and self.new_pos == 3:
            return self.animation_player(self.doors[1], "right_", 0, 3)

        elif self.old_pos == 3 and self.new_pos == 2:
            return self.animation_player("pc", "right_", 4, 2)

        elif self.old_pos == 2 and self.new_pos == 1:
            return self.animation_player(self.doors[0], "left_", 0, 1)

        elif self.old_pos == 1 and self.new_pos == 2:
            return self.animation_player("pc", "left_", 4, 2)

    def animation_player(
            self,
            fin_pos,
            frame,
            numeration,
            old_pos
    ):
        if self.frm_switch == False:
            self.frm_time = time()
            self.frm_switch = True

        if time() - self.frm_time > 0.0000001:
            self.frm_switch = False
            if self.frm_number == 4:
                self.frm_number = 1
                self.old_pos = old_pos
                return fin_pos
            else:
                self.frm_number += 1
                return frame + str(abs((self.frm_number - 1) - numeration))
