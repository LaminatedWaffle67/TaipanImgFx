from TaipanCode.Fileman.Display import images
import os, platform

image_count = 15

UserSys = platform.system()

if UserSys == "Windows":
    Username = os.getenv("USERNAME")

elif UserSys == "Darwin":
    Username = os.getenv("USER")

elif UserSys == "Linux":
    Username = os.getenv("USER")

else:
    raise("Uknown user OS")

folder_path = ""
image_file_path = ""