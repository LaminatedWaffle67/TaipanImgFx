from TaipanCode.Fileman.Display import images
from rich import print
import os, platform, sys, settings

def os_detect():
    user_os = platform.system()

    '''Pre OS logic variables'''
    image_list = []
    saved_image_list = []
    '''Pre OS logic variables'''

    if user_os == "Windows":
        username = os.getenv("USERNAME")
        directory_path = fr"C:\Users\{username}\Desktop\TaipanImgFx"

        image_folder_path = fr"TaipanCode\Fileman\Display\images"
        saved_image_folder_path = fr"TaipanCode\Fileman\Display\saved_images"


        image_directory_path = os.path.join(directory_path, image_folder_path)
        saved_image_directory_path = os.path.join(directory_path, saved_image_folder_path)

        if os.path.exists(image_directory_path):
            list_of_image_paths = os.listdir(image_directory_path)

            png_image_list = []
            for image_path_check in list_of_image_paths:
                _, ext = os.path.splitext(image_path_check)
                if ext.lower() == ".png":
                    png_image_list.append(image_path_check)

                else:
                    print ("Error")


            for image_path in png_image_list:
                image_file_path = os.path.join(image_directory_path, image_path)
                image_list.append(image_file_path)

        else:
            print (f"[red]Error: You are missing a required folder/file, the path to this folder/file is {image_directory_path} !TFE - Taipan File Error![/red]\n")
            
            if input("Input y if you want to reinstate this folder/file to continue despite the error.\n>").lower() == "y":
                os.makedirs(image_directory_path)

                if os.path.exists(image_directory_path):
                    listed_image_files = os.listdir(image_directory_path)

                    png_images = []
                    for image_check in listed_image_files:
                        _, ext = os.path.splitext(image_check)
                        if ext.lower() == ".png":
                            png_images.append(image_check)

                    for image_path in png_images:
                        image_file_path = os.path.join(image_directory_path, image_path)
                        image_list.append(image_file_path)

                else:
                    print (f"[red]Error: The folder/file reinstation failed, the path to this folder/file is {image_directory_path} and it is needed for TaipanImgFx to work properly !TFE - Taipan File Error![/red]\n")


            else:
                print("\n---PRE---ERROR---HISTORY---\n")

                try:
                    raise ValueError(f"Will add later")

                except ValueError as e:
                    print (f"Error: {e}")
                    sys.exit()

    elif user_os == "Darwin":
        username = os.getenv("USER")
        directory_path = f"/home/{username}/Desktop/TaipanImgFx"
        image_folder_path = "TaipanCode/Fileman/Display/images"

        image_directory_path = os.path.join(directory_path, image_folder_path)
        saved_image_directory_path = os.path.join(directory_path, f"TaipanCode/Fileman/Display/saved_images")

        if os.path.exists(image_directory_path):
            listed_image_files = os.listdir(image_directory_path)

            png_images = []
            for image_check in listed_image_files:
                _, ext = os.path.splitext(image_check)
                if ext.lower() == ".png":
                    png_images.append(image_check)
            

            for image_path in png_images:
                image_file_path = os.path.join(image_directory_path, image_path)
                image_list.append(image_file_path)

        else:
            print (f"[red]Error: You are missing a required folder/file, the path to this folder/file is {image_directory_path} !TFE - Taipan File Error![/red]\n")
            
            if input("Input y if you want to reinstate this folder/file to continue despite the error.\n>").lower() == "y":
                os.makedirs(image_directory_path)

                if os.path.exists(image_directory_path):
                    listed_image_files = os.listdir(image_directory_path)

                    png_images = []
                    for image_check in listed_image_files:
                        _, ext = os.path.splitext(image_check)
                        if ext.lower() == ".png":
                            png_images.append(image_check)

                    for image_path in png_images:
                        image_file_path = os.path.join(image_directory_path, image_path)
                        image_list.append(image_file_path)

                else:
                    print (f"[red]Error: The folder/file reinstation failed, the path to this folder/file is {image_directory_path} and it is needed for TaipanImgFx to work properly !TFE - Taipan File Error![/red]\n")


            else:
                print("\n---PRE---ERROR---HISTORY---\n")

                try:
                    raise ValueError(f"Will add later")

                except ValueError as e:
                    print (f"Error: {e}")
                    sys.exit()


    elif user_os == "Linux":
        username = os.getenv("USER")
        directory_path = f"/home/{username}/Desktop/TaipanImgFx"
        image_folder_path = "TaipanCode/Fileman/Display/images"

        image_directory_path = os.path.join(directory_path, image_folder_path)
        saved_image_directory_path = os.path.join(directory_path, f"TaipanCode/Fileman/Display/saved_images")
        
        if os.path.exists(image_directory_path):
            listed_image_files = os.listdir(image_directory_path)

            png_images = []
            for image_check in listed_image_files:
                _, ext = os.path.splitext(image_check)

                if ext.lower() == ".png":
                    png_images.append(image_check)
                
                else:
                    if settings.dev_mode:
                        print (f"Will add later ext = {ext}")



            for image_path in png_images:
                image_file_path = os.path.join(image_directory_path, image_path)
                image_list.append(image_file_path)
        
        else:
            print (f"[red]Error: You are missing a required folder/file, the path to this folder/file is {image_directory_path} !TFE - Taipan File Error![/red]\n")
            
            if input("Input y if you want to reinstate this folder/file to continue despite the error.\n>").lower() == "y":
                os.makedirs(image_directory_path)

                if os.path.exists(image_directory_path):
                    listed_image_files = os.listdir(image_directory_path)

                    png_images = []
                    for image_check in listed_image_files:
                        _, ext = os.path.splitext(image_check)
                        if ext.lower() == ".png":
                            png_images.append(image_check)

                    for image_path in png_images:
                        image_file_path = os.path.join(image_directory_path, image_path)
                        image_list.append(image_file_path)

                else:
                    print (f"[red]Error: The folder/file reinstation failed, the path to this folder/file is {image_directory_path} and it is needed for TaipanImgFx to work properly !TFE - Taipan File Error![/red]\n")


            else:
                print("\n---PRE---ERROR---HISTORY---\n")

                try:
                    raise ValueError(f"Will add later")

                except ValueError as e:
                    print (f"Error: {e}")
                    sys.exit()


    else:
        print (f"[red]Your Operating System is not supported by the software TaipanImgFx !TSE - Taipan System Error![/red]\n")
        print(f"The Operating System detected was '{user_os}'")
        print("\n---PRE---ERROR---HISTORY---\n")
        try:
            raise ValueError("Unknown user OS, the Operating System your computer is currently running is not compatible with TaipanImgFx, the supported Operating Systems are Windows, MacOS and Linux.")
        
        except ValueError as e:
            print (f"Error: {e}")
            sys.exit()
            


    if settings.additional_save_file != None:
        if os.path.exists(settings.additional_save_file):
            additional_save_file_path = settings.additional_save_file

        else:
            try:
                raise FileNotFoundError("Error")
            
            except FileNotFoundError as e:
                print(f"Error: {e}")
                sys.exit()
            
    return [image_directory_path]

    