import pygame, sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
import config
from rich import print

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

    screen.fill((config.bg_color))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()
    config.constructor.append(f"color.invert({red_strength}, {green_strength}, {blue_strength})")


def black_and_white(exclude_red: bool=False, exclude_green: bool=False, exclude_blue: bool=False) -> None:
    color_list = []

    for x in range(0, screen_width, 1):
        for y in range(0, screen_height, 1):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:
                brightness = (red * 0.3) + (green * 0.6) + (blue * 0.1)

                red = brightness if not exclude_red else red
                green = brightness if not exclude_green else green
                blue = brightness if not exclude_blue else blue

                color_list.append(((red, green, blue), (x, y)))


    screen.fill((config.bg_color))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()
    config.constructor.append(f"color.invert({exclude_red}, {exclude_green}, {exclude_blue})")


def isolate(exclude_red: bool=True, exclude_green: bool=False, exclude_blue: bool=False, option_index: int=1):
    color_list = []

    for x in range(0, screen_width, 1):
        for y in range(0, screen_height, 1):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:
                if option_index == 1:
                    if red > green and red > blue:
                        brightest_channel = red

                    elif green > red and green > blue:
                        brightest_channel = green

                    elif blue > red and blue > green:
                        brightest_channel = blue
                    
                    else:
                        brightest_channel = None

                    if brightest_channel == red and exclude_red:
                        red, green, blue = config.bg_color[0], config.bg_color[1], config.bg_color[2]

                    if brightest_channel == green and exclude_green:
                        red, green, blue = config.bg_color[0], config.bg_color[1], config.bg_color[2]

                    if brightest_channel == blue and exclude_blue:
                        red, green, blue = config.bg_color[0], config.bg_color[1], config.bg_color[2]
                    
                elif option_index == 2:
                    if red > green and red > blue:
                        brightest_channel = red

                    elif green > red and green > blue:
                        brightest_channel = green

                    elif blue > red and blue > green:
                        brightest_channel = blue

                    else:
                        brightest_channel = None

                    red = config.bg_color[0] if brightest_channel == red and exclude_red else red
                    green = config.bg_color[1] if brightest_channel == green and exclude_green else green
                    blue = config.bg_color[2] if brightest_channel == blue and exclude_blue else blue

                else:
                    print(f"Operation cancelled invalid option index {option_index} [red]TPE (Taipan Parameter Error[/red]")
                    raise RuntimeError("TPE inavlid option index")
                

                color_list.append(((red, green, blue), (x, y)))


    screen.fill((config.bg_color))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()
    config.constructor.append(f"color.invert({exclude_red}, {exclude_green}, {exclude_blue}, {option_index})")

def contrast(low_thresh: int=200, high_thresh: int=765, fill_color: tuple=(255, 255, 255), replace_color: tuple=config.bg_color):
    color_list = []

    for x in range(0, screen_width, 1):
        for y in range(0, screen_width, 1):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:
                brightness = red + green + blue

                if brightness >= low_thresh and brightness <= high_thresh:
                    color_list.append((fill_color, (x, y)))
                else:
                    color_list.append((replace_color, (x, y)))

    screen.fill((config.bg_color))
    for color, pos in color_list:
        screen.set_at((pos), color)
    pygame.display.update()
    config.constructor.append(f"color.invert({low_thresh}, {high_thresh}, {fill_color}, {replace_color})")