import pygame, os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(project_root)
import config
from TaipanCode.Fileman import storage
from rich import print

pygame.init()

def pygame_display() -> None:
    '''Will add PEP 257 docstrings soon'''
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if config.save_option:
                    current_stored_image = storage.save()
                    print (f"Image successfully saved at {current_stored_image}")

                running = False

    pygame.quit()


def load_image() -> None:
    '''Will add PEP 257 docstrings soon'''
    screen = config.screen
    joined_path = os.path.join(config.image_directory_path, f"TaipanImage{config.image_index}.png")

    try:
        current_image = pygame.image.load(joined_path)

    except FileNotFoundError:
        print (f"Chosen image path is invalid {joined_path} [red]TFE (Taipan File Error)[/red]")
        raise RuntimeError(f"TFE Chosen image path is invalid {joined_path}")

    if config.blit_x is None:
        config.blit_x = 0

    if config.blit_y is None:
        config.blit_y = 0

    blit_x, blit_y = config.blit_x, config.blit_y


    screen.blit(current_image, (blit_x, blit_y))
    pygame.display.update()