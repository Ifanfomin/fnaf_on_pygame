from pygame.image import load
from pygame import Surface, rect
from os import listdir


def load_images(
        path: str,
        WIDTH: int,
        HIGHT: int,
        alpha: int = 255,
        frames_type: str = "dict"
):
    if frames_type == "dict":
        files_names = listdir(path)
        frames = {}
        for file_name in files_names:
            title_surf = load(path + "/" + file_name).convert()
            title_rect = title_surf.get_rect(bottomright=(WIDTH, HIGHT))
            title_surf.set_alpha(alpha)
            frames[file_name] = [title_surf, title_rect]
            # screen.blit(title_surf, title_rect)
        return frames
    elif frames_type == "list":
        files_names = listdir(path)
        frames = []
        for file_name in files_names:
            title_surf = load(path + "/" + file_name).convert()
            title_rect = title_surf.get_rect(bottomright=(WIDTH, HIGHT))
            title_surf.set_alpha(alpha)
            frames.append([title_surf, title_rect])
            # screen.blit(title_surf, title_rect)
        return frames


def view_image(
        image: list[Surface, rect],
        screen: Surface
):
    screen.blit(image[0], image[1])
