'''Needed imports'''
import TaipanCode
import TaipanCode.Fileman as Fileman_folder
import TaipanCode.Fileman.Display as Display_folder
import TaipanCode.Fileman.Display.display as display
import config, pygame, os, settings
'''Needed imports'''

pygame.init()
config.screen_width = 800
config.screen_height = 800
config.blit_x = 200
config.blit_y = 200
config.bg_color = (0, 0, 0)

'''User input for image handling'''
image_upload = 0
if image_upload:
    import TaipanCode.Fileman.Display.image_upload as upload
    import config

user_input = 1
image_index = (int(input(f"Input image index from 1 to {config.image_count} or from -1 to -2\n>")), int(input(f"Pick 1 to have a save option and 0 for no option."))) if user_input == 0 else (15, 1)

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
spatial.transpose(2)
color.np_black_and_white(True, False, True)
color.converge(True, False, False, 255, 232, 150, 20, 2)
spatial.transpose(1)
'''User chosen effects'''

'''Image displaying'''
display.pygame_display()
'''Image displaying'''
