"""Shockwave is a simple game in which the objective is to make all the tiles the same color."""

import random
import pygame
from shockconst import *

class Score():
    def __init__(self):
        self.score = 0
        self.font = "comicsansms"
        self.text = pygame.font.SysFont(self.font,FONTSIZE)
        self.color = SCORECOLOR

    def render(self):
        txtsurf = self.text.render(str(self.score),False,self.color)
        return txtsurf

    def renderwin(self):
        if self.score > 1:
            vicmesg = "Game won in {} moves.".format(self.score)
        else:
            vicmesg = "Game won in 1 move."

        txtsurf = self.text.render(vicmesg,True,WHITE)
        return txtsurf

class Tile():
    """Represents the colored squares in the game."""

    def __init__(self,gridrow,gridcol):
        self.colored = False
        self.height = TILEHEIGHT
        self.width = TILEWIDTH
        self.rect = None
        self.gridrow = gridrow
        self.gridcol = gridcol

class Grid():
    """Represents the grid of tiles in the game."""

    def __init__(self,grid):
        self.grid = grid
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def flip_tile(self,tile):
        """Flips the colored attribute of a Tile object."""
        tile.colored = not tile.colored

    def flip_row(self, row):
        """Flips all tiles in a given row."""
        for tile in self.grid[row]:
            self.flip_tile(tile)
                     
    def flip_column(self, column):
        """Flips all tiles in a given column."""
        for row in self.grid:
            self.flip_tile(row[column])
    
    def flip_relative(self,row,column,direction,dist):
        """Flips a tile dist tiles away from the Tile location
        dictated by row & column, in direction."""
        if direction == "left":
            self.flip_tile(self.grid[row][column - dist])
        elif direction == "right":
            self.flip_tile(self.grid[row][column + dist])
        elif direction == "up":
            self.flip_tile(self.grid[row - dist][column])
        elif direction == "down":
            self.flip_tile(self.grid[row + dist][column])
    
    def randomize_tiles(self):
        """Randomizes grid tiles in a way that's solvable."""
        for row in self.grid:
            for tile in row:
                if random.randint(0,1) == 1:
                    self.flip_row(tile.gridrow)
                    self.flip_column(tile.gridcol)
	
    def assign_rects(self):
        """Assigns values to tile.rect attributes."""
        basex = 0
        basey = 0
        for row in self.grid:
            for tile in row:
                tile.rect = pygame.Rect(basex + XMARGIN,
                                        basey + YMARGIN,
                                        tile.width,tile.height)
                basex += (TILEGAP + tile.width)
            basex = 0
            basey += (TILEGAP + tile.height)
      
    def draw_grid(self,surface):
        """Draws Tiles to a surface from a Grid object."""
        for row in self.grid:
            for tile in row:
                pygame.draw.rect(surface,DEFTILECOLOR,tile.rect)


def create_grid(width,height):
    """Creates Grid holding a multidimensional array of Tile objects."""
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

def tile_at_location(grid,coords):
    """Checks if a tile is at a given coordinate."""
    for row in grid.grid:
        for tile in row:
            if tile.rect.collidepoint(coords[0],coords[1]):
                return tile
    return False

def game_won(grid):
    """Checks if all the game tiles are the same color."""
    start = grid.grid[0][0] # First tile in Grid.grid
    for row in grid.grid:
        for tile in row:
            if start.colored != tile.colored:
                return False
    return True

def play_beep():
    beep = pygame.mixer.Sound('beep.wav')
    beep.play()
    
