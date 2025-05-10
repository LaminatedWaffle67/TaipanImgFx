import os, pygame, PIL, shutil, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(project_root)
from rich import print
try:
    import config
except:
    raise ("No module named config")

path = input("Input file path\n>")

if os.path.exists(path):
    os_index = 1
    while os.path.exists(os.join(config.folder_path, f"TaipanImage{os_index}")):
        os_index += 1

        if os_index > 99:
            print ("Storage memory exceeded or folder does not exist [red]TME (Taipan Memory Error)[/red]")

    joined_image_path = os.join(config.folder_path(("TaipanImage" + str(os_index))))
    
    shutil.move(path, joined_image_path)
    if os.path.exists(joined_image_path):
        print(f"[green] Image succesfully uploaded to {joined_image_path}[/green]")


    else:
        raise ("Folder path does not eixts [red]TFE (Taipan File Error)[/red]")

    

else:
    print ("File path does not exist [red]TFE (Taipan File Error)[/red]")
    raise ("TFE error path does not exist")