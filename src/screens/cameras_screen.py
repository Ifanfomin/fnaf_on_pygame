from src.base_funcs import load_images, view_image
from pygame import mixer as Mixer
from pygame import event as Event
from pygame import Surface
from src.event_handler import EventHandler
from time import time


class CamerasScreen(object):
    def __init__(
            self,
            WIDTH: int,
            HEIGHT: int,
            main_screen: Surface
    ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.main_screen = main_screen
        self.cam_number = "1"
        self.cams_frames = load_images("media/images/office_screen_images/cameras/cams", WIDTH, HEIGHT)
        self.noise = True
        self.noise_frames = []
        for alpha in range(230, 250, 20):
            [self.noise_frames.append(frame) for frame in
             load_images("media/images/office_screen_images/cameras/noise", WIDTH, HEIGHT, alpha, "list")]
        for alpha in range(240, 120, -20):
            [self.noise_frames.append(frame) for frame in
             load_images("media/images/office_screen_images/cameras/noise", WIDTH, HEIGHT, alpha, "list")]
        self.noise_len = len(self.noise_frames)
        self.noise_num = 1
        self.noise_frm_time = 0.1

    def cameras_screen(
            self,
            event_wait: EventHandler
    ):

        view_image(self.cams_frames[f"cam_{self.cam_number}.png"], self.main_screen)
        # view_image(self.noise_frames[f"noise_{str(self.noise_frm_num)}.png"], self.main_screen)
        # print(self.noise_num)
        view_image(self.noise_frames[self.noise_num], self.main_screen)

        self.noise_player()

        return self.camera_handler(event_wait)

    def camera_handler(
            self,
            event_wait: EventHandler
    ):
        cam_number = event_wait.cameras_number_handler(Event.get())
        if cam_number == "pc_close":
            return "office"
        elif cam_number != None:
            # print(self.cam_number)
            self.cam_number = cam_number
            self.noise = True
            self.noise_num = 0

    def noise_player(self):
        if self.noise == False and time() - self.noise_frm_time > 0.00001:
            if self.noise_num != -5:
                self.noise_frm_time = time()
                self.noise_num -= 1
            else:
                self.noise_num = -1

        if self.noise == True and time() - self.noise_frm_time > 0.00001:
            if self.noise_num != self.noise_len - 1:
                self.noise_frm_time = time()
                # print(self.noise_num)
                self.noise_num += 1
            else:
                self.noise_num = -1
                self.noise = False
