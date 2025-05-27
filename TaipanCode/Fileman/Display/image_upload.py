import os, PIL, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(project_root)
import PIL.Image
from rich import print
import config

os.system('clear')
path = input("Input file path\n>")

valid_ext = [".jpeg", ".jpg", ".tiff", ".bmp", ".webp", ".png"]
_, ext = os.path.splitext(path)
ext = ext.lower()


def valid_image():
    _, ext = os.path.splitext(path)
    ext = ext.lower()
    if ext in valid_ext and ext != ".png":
        return 1
    
    if ext == ".png":
        return 0
    
    else:
        print (f"[red]Error: Unsupported file extension '{ext}'\nThe supported image extensions are {valid_ext} !TFE - Taipan File Error![/red]\n")
        
        if input("Input y if you want to attempt to continue despite the error.\n>").lower() == "y":
            return 1

        else:
            print("\n---PRE---ERROR---HISTORY---\n")

            try:
                raise ValueError(f"TFE Unsupported file extension '{ext}'.\nTry checking the file path and extension.\nIf the file format is unsupported you may be able to convert it using online tools.")

            except ValueError as e:
                print (f"Error: {e}")
                sys.exit()
        

def png_convert(output_path):
    if valid_image():
        with PIL.Image.open(path) as img:
            img.save(output_path, format="PNG")


if os.path.exists(path):
    print(f"{path} exists")
    if os.path.exists(config.image_directory_path):
        print(f"{config.image_directory_path} exists")
        os_index = 1
        while os.path.exists(os.path.join(config.image_directory_path, f"TaipanImage{os_index}.png")):
            print(f"The file TaipanImage{os_index}.png is taken, moving up 1.")
            os_index += 1

            if os_index > 99:
                print ("Error: Storage memory limit exceeded, the limit is 99 files saved [red]TME (Taipan Memory Error)[/red]")
                raise RuntimeError("TME error memory exceeded")

        joined_image_path = os.path.join(config.image_directory_path, ("TaipanImage" + str(os_index) + ".png"))
        
        png_convert(joined_image_path)
        if os.path.exists(joined_image_path):
            print(f"[green]Image successfully uploaded to {joined_image_path}[/green]")


        else:
            print ("Error: File was not uploaded successfully [red]TFE (Taipan File Error)[/red]")
            print (f"joined_image_path: {joined_image_path}\npath: {path}\nos_index: {os_index}\nconfig.image_directory_path: {config.image_directory_path}")
            raise RuntimeError("TFE upload unsuccesful")
    

else:
    print (f"Error: File path ({path}) does not exist [red]TFE (Taipan File Error)[/red]")
    raise FileNotFoundError("TFE error path does not exist")