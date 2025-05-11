import os, PIL, shutil, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(project_root)
import PIL.Image
from rich import print
import config

path = input("Input file path\n>")

valid_ext = [".png", ".jpeg", ".jpg", ".tiff", ".bmp"]
def valid_image():
    _, ext = os.path.splitext(path)
    return ext.lower() in valid_ext

def png_convert(output_path):
    if valid_image():
        with PIL.Image.open(path) as img:
            img.save(output_path, format="PNG")


if os.path.exists(path):
    print(f"{path} exists")
    if os.path.exists(config.folder_path):
        print(f"{config.folder_path} exists")
        os_index = 1
        while os.path.exists(os.path.join(config.folder_path, f"TaipanImage{os_index}")):
            print(f"{os_index}")
            os_index += 1

            if os_index > 99:
                print ("Error: Storage memory limit exceeded [red]TME (Taipan Memory Error)[/red]")
                raise RuntimeError("TME error memory exceeded")

        joined_image_path = os.path.join(config.folder_path, ("TaipanImage" + str(os_index)))
        
        png_convert(joined_image_path)
        if os.path.exists(joined_image_path):
            print(f"[green]Image successfully uploaded to {joined_image_path}[/green]")


        else:
            print ("Error: File was not uploaded successfully [red]TFE (Taipan File Error)[/red]")
            raise RuntimeError("TFE upload unsuccesful")
    

else:
    print (f"Error: File path ({path}) does not exist [red]TFE (Taipan File Error)[/red]")
    raise FileNotFoundError("TFE error path does not exist")