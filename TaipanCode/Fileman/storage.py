import pygame, sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
import config
from rich import print



def find_valid_path():
    screen = config.screen
    if os.path.exists(config.download_image_directory_path):
        print(f"{config.download_image_directory_path} exists")
        os_index = 1
        while os.path.exists(os.path.join(config.download_image_directory_path, f"TaipanDownloadImage{os_index}.png")):
            print(f"TaipanDownloadImage{os_index} is taken")
            os_index += 1

            if os_index > 99:
                print ("Error: Storage memory limit exceeded [red]TME (Taipan Memory Error)[/red]")
                raise RuntimeError("TME error memory exceeded")

        joined_image_path = os.path.join(config.download_image_directory_path, ("TaipanDownloadImage" + str(os_index) + ".png"))
        return joined_image_path
    
    else:
        print (f"Error: File path ({config.download_image_directory_path}) does not exist [red]TFE (Taipan File Error)[/red]")
        raise FileNotFoundError("TFE error path does not exist")
        


def download_screen():
    screen = config.screen
    path_validation = find_valid_path()
    pygame.image.save(screen, path_validation)
    return str(path_validation)
    



