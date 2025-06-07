import pygame, sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
import config



def clear(high_thresh: int, fill_color: tuple[int, int, int]=config.bg_color) -> None:
    print(config.screen)
    screen = config.screen
    screen_width, screen_height = config.screen_width, config.screen_height
    color_list = []

    for x in range(0, screen_height, 1):
        for y in range(0, screen_width, 1):
            red, green, blue, _ = screen.get_at((x, y))

            brightness = red + green + blue
            if brightness != 0:
                if brightness >= high_thresh or red == green and green == blue:
                    red = fill_color[0]
                    green = fill_color[1]
                    blue = fill_color[2]

                color_list.append(((red, green, blue), (x, y)))

    screen.fill((0, 0, 0))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()

def resize():
    pass

def translate():
    pass