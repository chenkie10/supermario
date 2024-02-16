import pygame
from source import constants as C
from source import tools

pygame.init()
SCREEN=pygame.display.set_mode((C.SCREEN_W,C.SCREEN_H))

GRAPHICS=tools.load_graphics('resources/graphics')