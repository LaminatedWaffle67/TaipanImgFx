import pygame, sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
import config, settings

def clear(low_thresh: int=0, high_thresh: int=255, fill_color: tuple[int, int, int]=config.bg_color, shade_range: int=0) -> None:
    screen = config.screen
    screen_width, screen_height = config.screen_width, config.screen_height
    color_list = []

    check_shade_range = lambda r, g, b: (abs(r - g) <= shade_range and abs(r - b) <= shade_range and abs(g - b) <= shade_range)
    for x in range(0, screen_height, 1):
        for y in range(0, screen_width, 1):
            red, green, blue, _ = screen.get_at((x, y))

            brightness = red + green + blue
            if brightness != 0:
                if brightness >= high_thresh or check_shade_range(red, green, blue):
                    red = fill_color[0]
                    green = fill_color[1]
                    blue = fill_color[2]

                color_list.append(((red, green, blue), (x, y)))

    screen.fill((0, 0, 0))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()



def lighten():
    pass

