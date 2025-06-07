import pygame, os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(project_root)
import config, settings
from TaipanCode.Fileman import storage
from rich import print
from config import effect_queue

pygame.init()

def pygame_display() -> None:
    '''Will add PEP 257 docstrings soon'''
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if config.save_option:
                    try:
                        save_confirmation = int(input("Type 1 to confirm save\n>"))
                        if save_confirmation == 1:
                            storage.download_screen()
                            print (f"Image successfully saved at additional path {config.saved_image_directory_path}")
                            print (f"Image successfully saved at additional path {config.additional_save_file_path}")
                    except TypeError:
                        pass
                    

                running = False

        while not effect_queue.empty():
            current_effect = effect_queue.get()
            current_effect()


    pygame.quit()


def load_image() -> None:
    '''Will add PEP 257 docstrings soon'''
    screen = config.screen
    if config.image_index >= 1:
        image_joined_path = os.path.join(config.image_directory_path, f"TaipanImage{config.image_index}.png")
    
    elif config.image_index == 0:
        image_joined_path = os.path.join(config.download_image_directory_path, f"TaipanDownloadImage{config.image_index}.png")
        
        try:
            constructor_joined_path = os.path.join(config.download_image_directory_path, f"TaipanDownloadConstructor{config.image_index}.txt")

            with open(constructor_joined_path, "r") as file:
                for line in file:
                    print (line)

        except:
            print ("Don't know what error this raises, will check later.")

    try:
        current_image = pygame.image.load(image_joined_path)

    except FileNotFoundError:
        print (f"Chosen image path is invalid {image_joined_path} [red]TFE (Taipan File Error)[/red]")
        raise RuntimeError(f"TFE Chosen image path is invalid {image_joined_path}")

    if config.blit_x is None:
        config.blit_x = 0

    if config.blit_y is None:
        config.blit_y = 0

    blit_x, blit_y = config.blit_x, config.blit_y


    screen.blit(current_image, (blit_x, blit_y))
    pygame.display.update()