import pygame, sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
import config

screen = config.screen
screen_width, screen_height = config.screen_width, config.screen_height

def invert(red_strength: int=255, green_strength: int=255, blue_strength: int=255):
    color_list = []

    for x in range(0, screen_width, 1):
        for y in range(0, screen_width, 1):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:
                red = max((red_strength - red), 0)
                red = min(red, 255)

                green = max((green_strength - green), 0)
                green = min(green, 255)

                blue = max((blue_strength - blue), 0)
                blue = min(blue, 255)

                color_list.append(((red, green, blue), (x, y)))

    screen.fill((0, 0, 0))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()