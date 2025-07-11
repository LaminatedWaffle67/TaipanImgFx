'''Needed imports'''
import TaipanCode
import TaipanCode.Fileman as Fileman_folder
import TaipanCode.Fileman.Display as Display_folder
import TaipanCode.Fileman.Display.display as display
import config, pygame, os, settings, gui, threading
from time import sleep
'''Needed imports'''

pygame.init()

'''User input for image handling'''
image_upload = 0
if image_upload:
    import TaipanCode.Fileman.Display.image_upload as upload

user_input = 1
image_index = (int(input(f"Input image index from 1 to {config.image_count} or from -1 to -2\n>")), int(input(f"Pick 1 to have a save option and 0 for no option."))) if user_input == 0 else (17, 0)

config.image_index = image_index[0]
screen = config.screen

import TaipanCode.AllEffects.edit as edit
import TaipanCode.AllEffects.color as color
import TaipanCode.AllEffects.spatial as spatial

config.save_option = False if image_index[1] == 0 else True

display.load_image()
'''User input for image handling'''

'''User chosen effects'''
if settings.alpha_test == "a":
    threading.Thread(target=gui.start_gui, daemon=True).start()

color.new_colorise(100, 3)
'''User chosen effects'''

'''Image displaying'''
display.pygame_display()
'''Image displaying'''
