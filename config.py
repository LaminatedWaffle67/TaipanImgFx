from TaipanCode.Fileman.Display import images
import os, platform



user_sys = platform.system()
username = None
directory_path = None
image_directory_path = None
image_list = []

if user_sys == "Windows":
    username = os.getenv("USERNAME")
    directory_path = fr"C:\Users\{username}\Desktop\TaipanImgFx"

    image_folder_path = fr"TaipanCode\Fileman\Display\images"

    image_directory_path = os.path.join(directory_path, image_folder_path)

    if os.path.exists(image_directory_path):
        listed_image_files = os.listdir(image_directory_path)

        for image_path in listed_image_files:
            image_file_path = os.path.join(image_directory_path, image_path)
            image_list.append(image_file_path)

elif user_sys == "Darwin":
    username = os.getenv("USER")
    directory_path = f"/home/{username}/Desktop/TaipanImgFx"
    image_folder_path = "TaipanCode/Fileman/Display/images"

    image_directory_path = os.path.join(directory_path, image_folder_path)

    if os.path.exists(image_directory_path):
        listed_image_files = os.listdir(image_directory_path)

        for image_path in listed_image_files:
            image_file_path = os.path.join(image_directory_path, image_path)
            image_list.append(image_file_path)


elif user_sys == "Linux":
    username = os.getenv("USER")
    directory_path = f"/home/{username}/Desktop/TaipanImgFx"
    image_folder_path = "TaipanCode/Fileman/Display/images"

    image_directory_path = os.path.join(directory_path, image_folder_path)

    if os.path.exists(image_directory_path):
        listed_image_files = os.listdir(image_directory_path)

        for image_path in listed_image_files:
            image_file_path = os.path.join(image_directory_path, image_path)
            image_list.append(image_file_path)


else:
    raise("Uknown user OS")

screen = None
screen_width = 0
screen_height = 0

image_count = len(image_list)
image_index = 0

blit_x = None
blit_y = None