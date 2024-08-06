import pygame
import time
from os import listdir


def load_images(path, WIDTH, HIGHT, alpha=255, type="dict"):
    if type == "dict":
        files_names = listdir(path)
        frames = {}
        for file_name in files_names:
            title_surf = pygame.image.load(path + "/" + file_name).convert()
            title_rect = title_surf.get_rect(bottomright=(WIDTH, HIGHT))
            title_surf.set_alpha(alpha)
            frames[file_name] = [title_surf, title_rect]
            # screen.blit(title_surf, title_rect)
        return frames
    elif type == "list":
        files_names = listdir(path)
        frames = []
        for file_name in files_names:
            title_surf = pygame.image.load(path + "/" + file_name).convert()
            title_rect = title_surf.get_rect(bottomright=(WIDTH, HIGHT))
            title_surf.set_alpha(alpha)
            frames.append([title_surf, title_rect])
            # screen.blit(title_surf, title_rect)
        return frames


def view_image(image, screen):
    screen.blit(image[0], image[1])




class TitleScreen(object):
    def __init__(self, WIDTH, HEIGHT, screen):
        self.main_screen = screen
        self.frm_number = 1
        self.frm_switch = False
        self.frm_time = 0
        self.frames = load_images("../media/images/title_screen_images", WIDTH, HEIGHT)
        pygame.mixer.music.load('media/sounds/title_screen_music_sin_nanna.mp3')
        pygame.mixer.music.play()

    def title_screen(self, event_wait):
        if self.frm_switch == False:
            self.frm_time = time.time()
            self.frm_switch = True
        if time.time() - self.frm_time > 0.03:
            self.frm_switch = False
            if self.frm_number == 5:
                self.frm_number = 1
            else:
                self.frm_number += 1

        view_image(self.frames[f"title_{str(self.frm_number)}.png"], self.main_screen)

        scene = event_wait.title_screen_handler(pygame.event.get())
        return scene


class NightPlay(object):
    def __init__(self, WIDTH, HEIGHT, main_screen):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.main_screen = main_screen
        self.night_screen = "office"
        self.office = OfficeScreen(self.WIDTH, self.HEIGHT, self.main_screen)
        self.cameras = CamerasScreen(self.WIDTH, self.HEIGHT, self.main_screen)

    def night_screen_switcher(self, event_wait):
        if self.night_screen == "office":
            night_screen = self.office.office_screen(event_wait)
            if night_screen != None:
                self.night_screen = night_screen

        elif self.night_screen == "cameras":
            night_screen = self.cameras.cameras_screen(event_wait)
            if night_screen != None:
                self.night_screen = night_screen


class CamerasScreen(object):
    def __init__(self, WIDTH, HEIGHT, main_screen):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.main_screen = main_screen
        self.cam_number = "1"
        self.cams_frames = load_images("../media/images/office_screen_images/cameras/cams", WIDTH, HEIGHT)
        self.noise = True
        self.noise_frames = []
        for alpha in range(230, 250, 20):
            [self.noise_frames.append(frame) for frame in
             load_images("../media/images/office_screen_images/cameras/noise", WIDTH, HEIGHT, alpha, "list")]
        for alpha in range(240, 120, -20):
            [self.noise_frames.append(frame) for frame in
             load_images("../media/images/office_screen_images/cameras/noise", WIDTH, HEIGHT, alpha, "list")]
        self.noise_len = len(self.noise_frames)
        self.noise_num = 1
        self.noise_frm_time = 0.1


    def cameras_screen(self, event_wait):

        view_image(self.cams_frames[f"cam_{self.cam_number}.png"], self.main_screen)
        # view_image(self.noise_frames[f"noise_{str(self.noise_frm_num)}.png"], self.main_screen)
        # print(self.noise_num)
        view_image(self.noise_frames[self.noise_num], self.main_screen)

        self.noise_player()

        return self.camera_handler(event_wait)

    def camera_handler(self, event_wait):
        cam_number = event_wait.cameras_number_handler(pygame.event.get())
        if cam_number == "pc_close":
            return "office"
        elif cam_number != None:
            # print(self.cam_number)
            self.cam_number = cam_number
            self.noise = True
            self.noise_num = 0


    def noise_player(self):
        if self.noise == False and time.time() - self.noise_frm_time > 0.00001:
            if self.noise_num != -5:
                self.noise_frm_time = time.time()
                self.noise_num -= 1
            else:
                self.noise_num = -1

        if self.noise == True and time.time() - self.noise_frm_time > 0.00001:
            if self.noise_num != self.noise_len - 1:
                self.noise_frm_time = time.time()
                # print(self.noise_num)
                self.noise_num += 1
            else:
                self.noise_num = -1
                self.noise = False


class OfficeScreen(object):
    def __init__(self, WIDTH, HEIGHT, main_screen):
        self.main_screen = main_screen
        self.frm_number = 1
        self.frm_switch = False
        self.frm_time = 0
        self.image = "pc"
        self.new_pos = 2  # части офиса слева направо от 1 до 3
        self.old_pos = 2
        self.light = "light"
        self.doors = ["left_4_open", "right_4_open"]
        self.light_on_off_sounds = [pygame.mixer.Sound("media/sounds/light_on_sound.wav"), pygame.mixer.Sound(
            "media/sounds/light_off_sound.wav")]
        self.frames = load_images("../media/images/office_screen_images/night_office", WIDTH, HEIGHT)

    def office_screen(self, event_wait):
        # print("Старая позиция: " + str(self.old_pos), "Новая позиция: " + str(self.new_pos))
        image = self.pos_handler()
        if image != None:
            self.image = image

        view_image(self.frames[f"{str(self.image)}_{self.light}.png"], self.main_screen)

        return self.action_handler(event_wait)

    def action_handler(self, event_wait):
        action = event_wait.office_screen_handler(pygame.event.get())
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

    def animation_player(self, fin_pos, frame, numeration, old_pos):
        if self.frm_switch == False:
            self.frm_time = time.time()
            self.frm_switch = True

        if time.time() - self.frm_time > 0.0000001:
            self.frm_switch = False
            if self.frm_number == 4:
                self.frm_number = 1
                self.old_pos = old_pos
                return fin_pos
            else:
                self.frm_number += 1
                return frame + str(abs((self.frm_number - 1) - numeration))
