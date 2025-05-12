'''Needed imports'''
import TaipanCode
import TaipanCode.Fileman
import TaipanCode.Fileman.Display
import TaipanCode.Fileman.Display.display
import config, pygame, os
'''Needed imports'''

pygame.init()
'''User input for image handling'''
image_upload = 0
if image_upload:
    import TaipanCode.Fileman.Display.image_upload as upload

user_input = 0
image_index = (int(input(f"Pick an image index from 0-{config.image_count}")), int(input(f"Pick 1 to have a save option and 0 for no option."))) if user_input == 0 else (0, 0)

if image_index[0] > config.image_count:
    image_index == config.image_count
    config.image_index = image_index

elif image_index[0] < 0:
    image_index = 0
    config.image_index = image_index

if image_index[1] < 0:
    image_index[1] = 0
    config.save_option = False

elif image_index[1] > 1:
    image_index[1] = 1
    config.save_option = True
'''User input for image handling'''

'''Image displaying'''
TaipanCode.Fileman.Display.display()
'''Image displaying'''
