import config, pygame, os

pygame.init()

user_input = 0
image_count = (int(input(f"Pick an image index from 0-{config.image_count}")), int(input(f"Pick 1 to have a save option and 0 for no option."))) if user_input == 0 else (0, 0)

print(image_count)