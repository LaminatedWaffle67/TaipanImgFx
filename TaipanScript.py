'''Needed imports'''
import TaipanCode
import TaipanCode.Fileman as Fileman_folder
import TaipanCode.Fileman.Display as Display_folder
import TaipanCode.Fileman.Display.display as display
import config, pygame, os, settings, subprocess, gui, threading
from time import sleep
'''Needed imports'''

pygame.init()
subprocess.run(["python3", "config.py"])
config.screen_width = 800
config.screen_height = 800
config.blit_x = 200
config.blit_y = 200
config.bg_color = (0, 0, 0)

'''User input for image handling'''
image_upload = 0
if image_upload:
    import TaipanCode.Fileman.Display.image_upload as upload
    subprocess.run(["python3", "config.py"])

user_input = 1
image_index = (int(input(f"Input image index from 1 to {config.image_count} or from -1 to -2\n>")), int(input(f"Pick 1 to have a save option and 0 for no option."))) if user_input == 0 else (15, 0)

config.image_index = image_index[0]

config.screen = pygame.display.set_mode((config.screen_width, config.screen_height))
screen = config.screen

import TaipanCode.AllEffects.edit as edit
import TaipanCode.AllEffects.color as color
import TaipanCode.AllEffects.spatial as spatial

config.save_option = False if image_index[1] == 0 else True

display.load_image()
'''User input for image handling'''

'''User chosen effects'''
if settings.alpha_test:
    threading.Thread(target=gui.start_gui, daemon=True).start()

'''User chosen effects'''

'''Image displaying'''
display.pygame_display()
'''Image displaying'''
