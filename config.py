import config_logic, settings, queue, pygame

os_detection_return = config_logic.os_detect()

bg_color = settings.default_bg
exlude_colors = [settings.default_exclude_colors] 

pygame.init()

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
screen_width = settings.screen_width
screen_height = settings.screen_height

image_count = os_detection_return[3]
image_index = None
saved_image_count = None

blit_x = settings.image_center_blit[0]
blit_y = settings.image_center_blit[1]

save_option = 0 

constructor = []

image_directory_path = os_detection_return[0]
saved_image_directory_path = os_detection_return[1]
additional_save_file_path = os_detection_return[2]

effect_queue = queue.Queue()

