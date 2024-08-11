import pygame
import sys


class EventHandler(object):
    @staticmethod
    def title_screen_handler(events: list):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_RETURN:  # return = enter
                    scene = "office"
                    pygame.mixer.music.stop()
                    print("Начало 1 ночи")
                    pygame.mixer.music.load("src/media/sounds/background_noise_sound.wav")
                    pygame.mixer.music.play(-1)
                    return scene

    @staticmethod
    def office_screen_handler(events: list):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_j:  # посмотреть вправо
                    return "right"
                elif event.key == pygame.K_d:  # посмотреть влево
                    return "left"
                elif event.key == pygame.K_l:  # переключить дверь справа (только если ты уже справа)
                    return "right_switched"
                elif event.key == pygame.K_a:  # переключить дверь слева (только если ты уже слева)
                    return "left_switched"
                elif event.key == pygame.K_SPACE:  # переключить свет (пока в любом месте)
                    return "light_switched"
                elif event.key == pygame.K_LSHIFT:  # открыть ЭВМ
                    return "pc_open"

    @staticmethod
    def cameras_number_handler(events: list):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_1:  # ловим выбранный номер камеры
                    return "1"
                elif event.key == pygame.K_2:
                    return "2"
                elif event.key == pygame.K_3:
                    return "3"
                elif event.key == pygame.K_4:
                    return "4"
                elif event.key == pygame.K_5:
                    return "5"
                elif event.key == pygame.K_6:
                    return "6"
                elif event.key == pygame.K_LSHIFT:  # открыть ЭВМ
                    return "pc_close"
