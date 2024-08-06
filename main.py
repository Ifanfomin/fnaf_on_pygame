from src.event_handler import EventHandler
from src.screens import *
import pygame


def main():
    pygame.init()

    WIDTH = 1920
    HEIGHT = 1080
    FPS = 30
    clock = pygame.time.Clock()
    main_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.toggle_fullscreen()
    pygame.mouse.set_visible(False)
    event_wait = EventHandler()
    scene = "title"

    title = TitleScreen(WIDTH, HEIGHT, main_screen)
    night = NightPlay(WIDTH, HEIGHT, main_screen)

    pygame.display.set_caption("FNAF")
    pygame.display.set_icon(pygame.image.load("media/images/icon.png"))  # my_fnaf/

    while True:
        if scene == "office":
            new_scene = night.night_screen_switcher(event_wait)
            if new_scene != None:
                scene = new_scene

        elif scene == "title":
            new_scene = title.title_screen(event_wait)
            if new_scene != None:
                scene = new_scene
                print(new_scene)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
