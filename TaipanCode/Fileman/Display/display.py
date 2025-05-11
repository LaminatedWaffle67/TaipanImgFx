import pygame, os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(project_root)
import config

pygame.init()

screen_width = config.screen_width
screen_height = config.screen_height
screen = config.screen

current_image = pygame.image.load(os.path.join(config.image_directory_path, f"TaipanImage{config.image_index}.png"))
if config.blit_x == None or config.blit_y == None:
    config.blit_x = 0 if config.blit_x == None else config.blit_x
    config.blit_y = 0 if config.blit_y == None else config.blit_y

blit_x = config.blit_x
blit_y = config.blit_y

screen.blit(current_image, (blit_x, blit_y))