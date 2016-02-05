from shockobjs import *
import pygame

pygame.init()

# create window
SCREEN = pygame.display.set_mode((WINSIZE,WINSIZE))
pygame.display.set_caption('Shockwave')
SCREEN.fill(BGCOLOR)

# create game grid
mainGrid = create_grid(GRIDSIZE,GRIDSIZE)
assign_rects(mainGrid.grid)
draw_grid(mainGrid.grid,SCREEN)

# randomize game grid
mainGrid.randomize_tiles()

while True: # main loop
    clickCoords = None
    # quit if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            clickCoords = event.pos
    
    # Checks if there's a tile at the clicked location.
    if clickCoords is not None:
        clickedTile = tile_at_location(mainGrid,clickCoords)
        if clickedTile is not False:
            for row in mainGrid.grid:
                for tile in row:
                    if clickedTile == tile:
                        mainGrid.flip_row(clickedTile.gridrow)
                        mainGrid.flip_column(clickedTile.gridcol)
    
    # Flips all tiles in a given clicked tile's row and column,
    # except for the one clicked.
    for row in mainGrid.grid:
        for tile in row:
            if tile.colored:
                SCREEN.fill(FLIPTILECOLOR,rect=tile.rect)
            else:
                SCREEN.fill(DEFTILECOLOR,rect=tile.rect)

    pygame.display.update()
