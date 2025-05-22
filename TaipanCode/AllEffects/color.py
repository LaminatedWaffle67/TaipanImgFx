import pygame, sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
import config, numpy
from rich import print

screen = config.screen
screen_width, screen_height = config.screen_width, config.screen_height

def np_invert(red_strength: float=1.0, green_strength: float=1.0, blue_strength: float=1.0):
    print("hi")
    if red_strength > 1.0:
        red_strength = 1.0
        print(f"Keep parameters to 0.0-1.0, you had a red_strength of {red_strength}")
    
    if red_strength < 0.0:
        red_strength = 0.0
        print(f"Keep parameters to 0.0-1.0, you had a red_strength of {red_strength}")

    if green_strength > 1.0:
        green_strength = 1.0
        print(f"Keep parameters to 0.0-1.0, you had a green_strength of {green_strength}")

    if green_strength < 0.0:
        green_strength = 0.0
        print(f"Keep parameters to 0.0-1.0, you had a green_strength of {green_strength}")

    if blue_strength > 1.0:
        blue_strength = 1.0
        print(f"Keep parameters to 0.0-1.0, you had a blue_strength of {blue_strength}")

    if blue_strength < 0.0:
        blue_strength = 0.0
        print(f"Keep parameters to 0.0-1.0, you had a blue_strength of {blue_strength}")


    screen_numpy_arr = pygame.surfarray.array3d(screen)
    bg_arr = numpy.array(config.bg_color, dtype = screen_numpy_arr.dtype)

    masked_arr = numpy.any(screen_numpy_arr != bg_arr, axis=2)
    inverted_arr = screen_numpy_arr.astype(dtype=numpy.float32).copy()
    
    inverted_arr[masked_arr, 0] = screen_numpy_arr[masked_arr, 0] * (1 - 2 * red_strength) + 255 * red_strength
    inverted_arr[masked_arr, 1] = screen_numpy_arr[masked_arr, 1] * (1 - 2 * green_strength) + 255 * green_strength
    inverted_arr[masked_arr, 2] = screen_numpy_arr[masked_arr, 2] * (1 - 2 * blue_strength) + 255 * blue_strength

    inverted_arr = numpy.clip(inverted_arr, 0, 255).astype(numpy.uint8)

    screen_numpy_arr[masked_arr] = inverted_arr[masked_arr]

    pygame.surfarray.blit_array(screen, screen_numpy_arr)
    pygame.display.update()


def invert(red_strength: int=255, green_strength: int=255, blue_strength: int=255, effect_x_step: int=1, effect_y_step: int=1):
    color_list = []

    for x in range(0, screen_width, effect_x_step):
        for y in range(0, screen_width, effect_y_step):
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
    config.constructor.append(f"color.invert({red_strength}, {green_strength}, {blue_strength})\n")


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
    config.constructor.append(f"color.invert({exclude_red}, {exclude_green}, {exclude_blue})\n")


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
    config.constructor.append(f"color.invert({exclude_red}, {exclude_green}, {exclude_blue}, {option_index})\n")

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
    config.constructor.append(f"color.invert({low_thresh}, {high_thresh}, {fill_color}, {replace_color})\n")

