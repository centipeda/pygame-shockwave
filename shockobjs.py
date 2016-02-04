"""Shockwave is a simple game that is based on flipping tiles in a square grid."""

import sys
import random

import pygame


DEFTILECOLOR = (255,0,0)
FLIPTILECOLOR = (0,255,255)
XMARGIN = 100
YMARGIN = 100
XTILEGAP = 10
YTILEGAP = 10
GRIDSIZE = 5

class Tile():
    def __init__(self,gridrow,gridcol):
        self.colored = False
        self.height = 50
        self.width = 50
        self.rect = None
        self.gridrow = gridrow
        self.gridcol = gridcol
class Grid():
    def __init__(self,grid):
        self.grid = grid
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        
    def get_row(self,row):
        return self.grid[row]
    
    def get_column(self,column):
        c = []
        for r in self.grid:
            c.append(r[column])
        return c

    def get_tile(self,row,column):
        return self.grid[row][column]

    def flip_tile(self,tile):
        tile.colored = not tile.colored

    def flip_row(self, row):
        for tile in self.grid[row]:
            self.flip_tile(tile)
                     
    def flip_column(self, column):
        for row in self.grid:
            self.flip_tile(row[column])
    
    def randomize_tiles(self):
        for row in self.grid:
            for tile in row:
                if random.randint(0,1) == 1:
                    self.flip_row(tile.gridrow)
                    self.flip_column(tile.gridcol)

def create_grid(width,height):
    # Creates multidimensional array of Tile objects.
    fullG = []
    # Used for incrementing.
    r = 0
    c = 0
    for row in range(height):
        row = []
        for column in range(width):
            row.append(Tile(r,c))
            c += 1
        c = 0
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

def tile_at_location(grid,coords):
    for row in grid.grid:
        for tile in row:
            if tile.rect.collidepoint(coords[0],coords[1]):
                return tile
    return False
