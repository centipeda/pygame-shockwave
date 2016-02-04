from shockobjs import *
import pygame
BGCOLOR = (255,255,255)

pygame.init()

# create window
SCREEN = pygame.display.set_mode((500,500))
pygame.display.set_caption('Shockwave')
SCREEN.fill(BGCOLOR)

# create game grid
mainGrid = create_grid(GRIDSIZE,GRIDSIZE)
assign_rects(mainGrid.grid)
draw_grid(mainGrid.grid,SCREEN)

while True: # main loop
    clickCoords = None
    # quit if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            clickCoords = event.pos
    
    if clickCoords is not None:
        clickedTile = tile_at_location(mainGrid,clickCoords)
        if clickedTile is not False:
            for row in mainGrid.grid:
                for tile in row:
                    if clickedTile == tile:
                        mainGrid.flip_row(clickedTile.gridrow)
                        mainGrid.flip_column(clickedTile.gridcol)

    for row in mainGrid.grid:
        for tile in row:
            if tile.colored:
                SCREEN.fill(FLIPTILECOLOR,rect=tile.rect)
            else:
                SCREEN.fill(DEFTILECOLOR,rect=tile.rect)

    pygame.display.update()
