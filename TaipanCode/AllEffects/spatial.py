import pygame, sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
import config

screen = config.screen
screen_width, screen_height = config.screen_width, config.screen_height

def transpose() -> None:
    color_list = []

    for x in range(0, screen_width, 1):
        for y in range(0, screen_width, 1):
            red, green, blue, _ = screen.get_at((x, y))
            x_position, y_position = x, y

            if (red, green, blue) != config.bg_color:
                brightest_channel = max(red, green, blue)

                if brightest_channel == red:
                    green = 255 - blue
                    blue = 255 - green
                    x_position -= red

                elif brightest_channel == green:
                    red = 255 - blue
                    blue = 255 - red
                    y_position += green

                elif brightest_channel == blue:
                    red = 255 - green
                    green = 255 - red
                    y_position -= blue

                color_list.append(((red, green, blue), (x_position, y_position)))


    screen.fill((0, 0, 0))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()
