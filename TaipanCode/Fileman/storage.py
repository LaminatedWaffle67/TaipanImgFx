import pygame, sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
import config, settings
from rich import print



def find_valid_path():
    screen = config.screen
    if os.path.exists(config.saved_image_directory_path):
        print(f"{config.saved_image_directory_path} exists")
        os_index = 1
        while os.path.exists(os.path.join(config.saved_image_directory_path, f"TaipanDownloadImage{os_index}.png")):
            print(f"TaipanDownloadImage{os_index} is taken")
            os_index += 1

            if os_index > 99:
                print ("Error: Storage memory limit exceeded [red]TME (Taipan Memory Error)[/red]")
                raise RuntimeError("TME error memory exceeded")

        joined_image_path = os.path.join(config.saved_image_directory_path, ("TaipanDownloadImage" + str(os_index) + ".png"))
        joined_constructor_path = os.path.join(config.saved_image_directory_path, ("TaipanDownloadConstructor" + str(os_index) + ".txt"))
        return joined_image_path, joined_constructor_path
    
    else:
        print (f"Error: File path ({config.saved_image_directory_path}) does not exist [red]TFE (Taipan File Error)[/red]")
        raise FileNotFoundError("TFE error path does not exist")
    
def additional_find_valid_path(save_file_path):
    screen = config.screen
    if os.path.exists(save_file_path):
        print(f"{save_file_path} exists")
        os_index = 1
        while os.path.exists(os.path.join(save_file_path, f"{settings.additional_save_file_name}{os_index}.png")):
            print(f"TaipanDownloadImage{os_index} is taken")
            os_index += 1

            if os_index > 99:
                print ("Error: Storage memory limit exceeded [red]TME (Taipan Memory Error)[/red]")
                raise RuntimeError("TME error memory exceeded")

        joined_image_path = os.path.join(save_file_path, (str(f"{settings.additional_save_file_name}") + str(os_index) + ".png"))
        return joined_image_path
    
    else:
        print (f"Error: File path ({save_file_path}) does not exist [red]TFE (Taipan File Error)[/red]")
        raise FileNotFoundError("TFE error path does not exist")
        


def download_screen():
    try:
        screen = config.screen
        image_save_file, constructor_save_file = find_valid_path()
        pygame.image.save(screen, image_save_file)
        with open(constructor_save_file, "w") as file:
            file.write(str(config.constructor))
        with open(constructor_save_file, "r") as file:
            print(file.read())

    except Exception as e:
        print(f"Error: {e}")
        sys.exit()


    if config.additional_save_file_path != None:
        try:
            screen = config.screen
            image_save_file = additional_find_valid_path(config.additional_save_file_path)
            pygame.image.save(screen, image_save_file)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit()
    



