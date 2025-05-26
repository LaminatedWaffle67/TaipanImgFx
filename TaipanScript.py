'''Needed imports'''
import TaipanCode
import TaipanCode.Fileman as Fileman_folder
import TaipanCode.Fileman.Display as Display_folder
import TaipanCode.Fileman.Display.display as display
import config, pygame, os
'''Needed imports'''

pygame.init()
config.screen_width = 800
config.screen_height = 800
config.blit_x = 150
config.blit_y = 40
config.screen = pygame.display.set_mode((config.screen_width, config.screen_height))

screen = config.screen

import TaipanCode.AllEffects.edit as edit
import TaipanCode.AllEffects.color as color
import TaipanCode.AllEffects.spatial as spatial

'''User input for image handling'''
image_upload = 0
if image_upload:
    import TaipanCode.Fileman.Display.image_upload as upload

user_input = 1
image_index = (int(input(f"Pick an image index from 1-{config.image_count}")), int(input(f"Pick 1 to have a save option and 0 for no option."))) if user_input == 0 else (7, 1)

if image_index[0] > config.image_count:
    image_index[0] = config.image_count

elif image_index[0] < 1:
    image_index[0] = 1

config.image_index = image_index[0]

if image_index[1] < 0:
    image_index[1] = 0


elif image_index[1] > 1:
    image_index[1] = 1

config.save_option = False if image_index[1] == 0 else True
display.load_image()
'''User input for image handling'''

'''User chosen effects'''

color.isolate(True, True, True, 2)
color.np_invert()
spatial.transpose(2)
color.isolate(False, True, True, 1)
color.isolate(True, False, False, 2)
'''User chosen effects'''

'''Image displaying'''
display.pygame_display()
'''Image displaying'''
