"""There isn't going to be much here for a while.

Shockwave is a simple game that is based on flipping tiles in a square grid.
"""

import pygame,sys
pygame.init()

BGCOLOR = (255,255,255)

# create window
mainDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption('Shockwave')

while True: # main loop

    # quit if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()

class Tile():
    def __init__(self):
        pass

class Grid(array):
    def __init__(self):
        self.grid = array
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        
    def get_row(self,row):
        pass
    
    def get_column(self,column):
        pass

    def get_tile(self,row,column):
        pass

    def is_colored(self,tile):
        pass

    def flip_tile(self,tile):
        pass

def create_grid(width,height):
    # Creates multidimensional array of Tile objects.
    fullG = []
    # Used for incrementing.
    r = 0
    c = 0
    for row in range(height):
        row = []
        for column in range(width):
            row.append(Tile())
            c += 1
        fullG.append(row)
        r += 1
    return Grid(fullG)
