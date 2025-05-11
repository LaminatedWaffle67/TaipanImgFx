from TaipanCode.Fileman.Display import images
import os, platform

image_count = 15

user_sys = platform.system()
username = None
directory_path = None
folder_path = None
image_file_path = None

if user_sys == "Windows":
    username = os.getenv("USERNAME")
    directory_path = fr"C:\Users\{username}\Desktop\taipan"

elif user_sys == "Darwin":
    username = os.getenv("USER")
    directory_path = fr"C:\Users\{username}\Desktop\taipan"

elif user_sys == "Linux":
    username = os.getenv("USER")
    directory_path = fr"C:\Users\{username}\Desktop\taipan"

else:
    raise("Uknown user OS")

