import pygame, sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
import config, numpy, settings, random
from rich import print

screen = config.screen
screen_width, screen_height = config.screen_width, config.screen_height

def np_invert(red_strength: float=1.0, green_strength: float=1.0, blue_strength: float=1.0) -> None:

    red_strength = numpy.clip(red_strength, 0.0, 1.0)
    green_strength = numpy.clip(green_strength, 0.0, 1.0)
    blue_strength = numpy.clip(blue_strength, 0.0, 1.0)

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
    config.constructor.append(f"color.np_invert({red_strength}, {green_strength}, {blue_strength})\n")


def invert(red_strength: int=255, green_strength: int=255, blue_strength: int=255) -> None:
    color_list = []

    for x in range(0, screen_width, settings.x_step):
        for y in range(0, screen_height, settings.y_step):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:
                red = max((red_strength - red), 0)
                red = min(red, 255)

                green = max((green_strength - green), 0)
                green = min(green, 255)

                blue = max((blue_strength - blue), 0)
                blue = min(blue, 255)

                color_list.append(((red, green, blue), (x, y)))

    if settings.fill_bg_over_step:
        screen.fill((config.bg_color))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()
    config.constructor.append(f"color.invert({red_strength}, {green_strength}, {blue_strength})\n")

def np_black_and_white(exclude_red: bool=False, exclude_green: bool=False, exclude_blue: bool=False) -> None:
    screen_numpy_arr = pygame.surfarray.array3d(screen)
    bg_arr = numpy.array(config.bg_color, dtype = screen_numpy_arr.dtype)

    masked_arr = numpy.any(screen_numpy_arr != bg_arr, axis=2)
    greyscale_arr = screen_numpy_arr.astype(dtype=numpy.float32).copy()

    brightness = (screen_numpy_arr[:, :, 0] * 0.3) + (screen_numpy_arr[:, :, 1] * 0.6) + (screen_numpy_arr[:, :, 2] * 0.1)
    
    if not exclude_red:
        greyscale_arr[..., 0][masked_arr] = brightness[masked_arr]

    if not exclude_green:
        greyscale_arr[..., 1][masked_arr] = brightness[masked_arr]

    if not exclude_blue:
        greyscale_arr[..., 2][masked_arr] = brightness[masked_arr]

    greyscale_arr = numpy.clip(greyscale_arr, 0, 255).astype(numpy.uint8)

    screen_numpy_arr[masked_arr] = greyscale_arr[masked_arr]

    pygame.surfarray.blit_array(screen, screen_numpy_arr)
    pygame.display.update()
    config.constructor.append(f"color.np_black_and_white({exclude_red}, {exclude_green}, {exclude_blue})\n")


def black_and_white(exclude_red: bool=False, exclude_green: bool=False, exclude_blue: bool=False) -> None:
    color_list = []

    for x in range(0, screen_width, ):
        for y in range(0, screen_height, settings.y_step):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:
                brightness = (red * 0.3) + (green * 0.6) + (blue * 0.1)

                red = brightness if not exclude_red else red
                green = brightness if not exclude_green else green
                blue = brightness if not exclude_blue else blue

                color_list.append(((red, green, blue), (x, y)))


    if settings.fill_bg_over_step:
        screen.fill((config.bg_color))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()
    config.constructor.append(f"color.black_and_white({exclude_red}, {exclude_green}, {exclude_blue})\n")

def np_isolate():
    screen_numpy_arr = pygame.surfarray.array3d(screen)

    bg_color_arr = numpy.array(config.bg_color, dtype=screen_numpy_arr.dtype)
    bg_color_mask = numpy.any(screen_numpy_arr != bg_color_arr, axis=2)

    if screen_numpy_arr[bg_color_mask][..., 0] > screen_numpy_arr[bg_color_mask][..., 1] > screen_numpy_arr[bg_color_mask][..., 2]:
        brightest_channel = screen_numpy_arr[bg_color_mask][..., 0]

    elif screen_numpy_arr[bg_color_mask][..., 1] > screen_numpy_arr[bg_color_mask][..., 0] > screen_numpy_arr[bg_color_mask][..., 2]:
        brightest_channel = screen_numpy_arr[bg_color_mask][..., 1]

    elif screen_numpy_arr[bg_color_mask][..., 2] > screen_numpy_arr[bg_color_mask][..., 0] > screen_numpy_arr[bg_color_mask][..., 1]:
        brightest_channel = screen_numpy_arr[bg_color_mask][..., 2]


def isolate(exclude_red: bool=True, exclude_green: bool=False, exclude_blue: bool=False, option_index: int=1):
    color_list = []

    for x in range(0, screen_width, settings.x_step):
        for y in range(0, screen_height, settings.y_step):
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


    if settings.fill_bg_over_step:
        screen.fill((config.bg_color))
    for color, pos in color_list:
        screen.set_at((pos), (color))

    pygame.display.update()
    config.constructor.append(f"color.invert({exclude_red}, {exclude_green}, {exclude_blue}, {option_index})\n")


def np_contrast():
    screen_numpy_arr = pygame.surfarray.array3d(screen)
    
    bg_numpy_arr = numpy.array(config.bg_color, dtype=numpy.uint8)

    bg_mask = numpy.any(screen_numpy_arr != bg_numpy_arr, axis=2)

    brightness = numpy.sum(screen_numpy_arr, axis=2)

    contrast_array = numpy.where(brightness > 200, 255, 0).astype(dtype=numpy.uint8)

    screen_numpy_arr[..., 0][bg_mask] = contrast_array[bg_mask]
    screen_numpy_arr[..., 1][bg_mask] = contrast_array[bg_mask]
    screen_numpy_arr[..., 2][bg_mask] = contrast_array[bg_mask]

    pygame.surfarray.blit_array(screen, screen_numpy_arr)
    pygame.display.update()

def contrast(low_thresh: int=200, high_thresh: int=765, fill_color: tuple=(255, 255, 255), replace_color: tuple=config.bg_color):
    color_list = []

    for x in range(0, screen_width, settings.x_step):
        for y in range(0, screen_height, settings.y_step):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:
                brightness = red + green + blue

                if brightness >= low_thresh and brightness <= high_thresh:
                    color_list.append((fill_color, (x, y)))
                else:
                    color_list.append((replace_color, (x, y)))

    if settings.fill_bg_over_step:
        screen.fill((config.bg_color))
    for color, pos in color_list:
        screen.set_at((pos), color)
    pygame.display.update()
    config.constructor.append(f"color.invert({low_thresh}, {high_thresh}, {fill_color}, {replace_color})\n")


def converge(red_focus: bool=True, green_focus: bool=False, blue_focus: bool=False, strength: int=255, red_replace_color: int=0, green_replace_color: int=0, blue_replace_color: int=0, option_index: int=1):
    color_list = []

    for x in range(0, screen_width, settings.x_step):
        for y in range(0, screen_height, settings.y_step):
            r, g, b, _ = screen.get_at((x, y))

            brightness = r + g + b

            if (r, g, b) != config.bg_color:
                norm_brightness = min((brightness / strength), 1)
                norm_brightness *= strength
                norm_brightness = int(norm_brightness)
                
                if option_index == 1:
                    if red_focus == True:
                        r = norm_brightness
                        g, b = green_replace_color, blue_replace_color

                    elif green_focus == True:
                        g = norm_brightness
                        r, b = red_replace_color, blue_replace_color

                    elif blue_focus == True:
                        b = norm_brightness
                        r, g = red_replace_color, blue_replace_color

                elif option_index == 2:
                    if red_focus == True:
                        r = norm_brightness

                    elif green_focus == True:
                        g = norm_brightness

                    elif blue_focus == True:
                        b = norm_brightness

                color_list.append(((x, y), (r, g, b)))

    if settings.fill_bg_over_step:
        screen.fill((config.bg_color))
    for pos, color in color_list:
        screen.set_at(pos, color)
    pygame.display.update()
    config.constructor.append(f"color.converge({red_focus}, {green_focus}, {blue_focus}, {strength}, {red_replace_color}, {green_replace_color}, {blue_replace_color}\n")


def np_polarise(red_to_blue: bool=True, blue_to_red: bool=False) -> None:
    screen_numpy_arr = pygame.surfarray.array3d(screen)
    
    bg_numpy_arr = numpy.array(config.bg_color, dtype=numpy.uint8)

    bg_mask = numpy.any(screen_numpy_arr != bg_numpy_arr, axis=2)


def polarise(red_to_blue: bool=True, blue_to_red: bool=False, red_fill_color: int=0, blue_fill_color: int=0, option_index: int=1) -> None:
    color_list = []

    for x in range(0, screen_width, settings.x_step):
        for y in range(0, screen_height, settings.y_step):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:
                if red > blue:
                    if option_index == 1:
                        blue = red
                        red = red_fill_color
                    elif option_index == 2:
                        blue = red

                elif blue > red:
                    if option_index == 1:
                        red = blue
                        blue = blue_fill_color
                    elif option_index == 2:
                        red = blue

                color_list.append(((x, y), (red, green, blue)))

    if settings.fill_bg_over_step:
        screen.fill((config.bg_color))
    for pos, color in color_list:
        screen.set_at(pos, color)
    pygame.display.update()
    config.constructor.append(f"color.polarise()")


def all_polarise(red_to_blue: bool=True, blue_to_red: bool=False, green_to_red: bool=False, red_to_green: bool=False, green_to_blue: bool=False, blue_to_green: bool=True, red_fill_color: int=0, blue_fill_color: int=0, green_fill_color: int=0, option_index: int=1) -> None:
    color_list = []

    for x in range(0, screen_width, settings.x_step):
        for y in range(0, screen_height, settings.y_step):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:
                pre_red = red
                pre_green = green
                pre_blue = blue

                if pre_red > green:
                    if red_to_green:
                        if option_index == 1:
                            green = pre_red
                            red = red_fill_color
                        elif option_index == 2:
                            green = pre_red


                if pre_red > pre_blue:
                    if red_to_blue:
                        if option_index == 1:
                            blue = pre_red
                            red = red_fill_color
                        elif option_index == 2:
                            blue = pre_red

                if pre_green > pre_red:
                    if green_to_red:
                        if option_index == 1:
                            red = pre_green
                            green = green_fill_color
                        elif option_index == 2:
                            red = pre_green

                if pre_green > pre_blue:
                    if green_to_blue:
                        if option_index == 1:
                            blue = pre_green
                            green = green_fill_color
                        elif option_index == 2:
                            blue = pre_green
                
                if pre_blue > pre_red:
                    if option_index == 1:
                        red = pre_blue
                        blue = blue_fill_color
                    elif option_index == 2:
                        red = pre_blue

                if pre_blue > pre_green:
                    if option_index == 1:
                        green = pre_blue
                        blue = blue_fill_color
                    elif option_index == 2:
                        green = pre_blue

                color_list.append(((x, y), (red, green, blue)))

    if settings.fill_bg_over_step:
        screen.fill((config.bg_color))
    for pos, color in color_list:
        screen.set_at(pos, color)
    pygame.display.update()
    config.constructor.append(f"color.polarise()")


def tone_shift(low_range: int=10, high_range: int=10, exclude_red: bool=False, exclude_green: bool=False, exclude_blue: bool=False):
    color_list = []

    for x in range(0, screen_width, settings.x_step):
        for y in range(0, screen_height, settings.y_step):
            red, green, blue, _ = screen.get_at((x, y))

            if (red, green, blue) != config.bg_color:

                if not exclude_red:
                    low_red, high_red  = red - low_range, red + high_range
                    low_red = numpy.clip(low_red, 0, 255)
                    high_red = numpy.clip(high_red, 0, 255)
                    red = random.randint(low_red, high_red)

                if not exclude_green:
                    low_green, high_green = green - low_range, green + high_range
                    low_green = numpy.clip(low_green, 0, 255)
                    high_green = numpy.clip(high_green, 0, 255)
                    green = random.randint(low_green, green)

                if not exclude_blue:
                    low_blue, high_blue  = blue - low_range, blue + high_range
                    low_blue = numpy.clip(low_blue, 0, 255)
                    high_blue = numpy.clip(high_blue, 0, 255)
                    blue = random.randint(low_blue, high_blue)
                
                color_list.append(((x, y), (red, green, blue)))

    if settings.fill_bg_over_step:
        screen.fill((config.bg_color))
    for pos, color in color_list:
        screen.set_at(pos, color)
    pygame.display.update()
    config.constructor.append(f"color.polarise()")