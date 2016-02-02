"""There isn't going to be much here for a while.

Shockwave is a simple game that is based on flipping tiles in a square grid.
"""

import pygame,sys

DEFTILECOLOR = (255,0,0)
FLIPTILECOLOR = (0,255,255)
XMARGIN = 100
YMARGIN = 100
XTILEGAP = 10
YTILEGAP = 10
GRIDSIZE = 5

class Tile():
    def __init__(self):
        self.colored = False
        self.height = 50
        self.width = 50
        self.rect = None

class Grid():
    def __init__(self,grid):
        self.grid = grid
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

def assign_rects(grid):
    basex = 1
    basey = 1
    for row in grid:
        for tile in row:
            tile.rect = pygame.Rect(basex + XMARGIN,basey + YMARGIN,
                             tile.width,tile.height)
            basex += (XTILEGAP + tile.width)
        basex = 1
        basey += (YTILEGAP + tile.height)

def draw_grid(grid,surface):
    for row in grid:
        for tile in row:
            pygame.draw.rect(surface,DEFTILECOLOR,tile.rect)
