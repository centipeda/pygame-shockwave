"""Contains constants for Shockwave."""
import random
import pygame

# Engine constants
FPS = 30
FLIPFRAME = 2

# miscellaneous constants
NAME = "Shockwave"

# color constants
def random_color():
    return (random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255))
BLACK = (0,0,0)
WHITE = (255,255,255)
BGCOLOR = BLACK
DEFTILECOLOR = random_color()
FLIPTILECOLOR = random_color()
SCORECOLOR = WHITE

# size-related constants
FONTSIZE = 30
GRIDH = 10
GRIDW = 10
XMARGIN = 40
YMARGIN = 40
TILEGAP = 2
TILEWIDTH = 30
TILEHEIGHT = 30
# fits window size to grid
WINW = ((XMARGIN * 2) + ((TILEWIDTH + TILEGAP) * GRIDW))
WINH = ((YMARGIN * 2) + ((TILEHEIGHT + TILEGAP) * GRIDH))
# main window
SCREEN = pygame.display.set_mode((WINW,WINH))


