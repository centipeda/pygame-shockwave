#!/usr/bin/env python

from shockobjs import *
import pygame

pygame.init()

# All constants referenced are stored in the shockobjs.py file.

def main():
    # Creating window.
    SCREEN = pygame.display.set_mode((WINW,WINH))
    pygame.display.set_caption(NAME)
    SCREEN.fill(BGCOLOR)

    # Creating game grid.
    mainGrid = create_grid(GRIDW,GRIDH)
    mainGrid.assign_rects()
    mainGrid.draw_grid(SCREEN)

    # Drawing score counter.
    scorecount = Score()
    scorerect = SCREEN.blit(scorecount.render(),(5,5))

    # Randomizing tiles.
    mainGrid.randomize_tiles()

    # For victory-checking.
    won = False

    while True: # main loop
        clickCoords = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                clickCoords = event.pos

        # Checks if there's a tile at the clicked location.
        # If so, flips tiles.
        if clickCoords is not None:
            clickedTile = tile_at_location(mainGrid,clickCoords)
            if clickedTile is not False:
                for row in mainGrid.grid:
                    for tile in row:
                        if clickedTile == tile:
                            play_beep()
                            mainGrid.flip_row(clickedTile.gridrow)
                            mainGrid.flip_column(clickedTile.gridcol)
                            scorecount.count += 1

        # Updates score count on board, or displays victory message.
        if not won:
            SCREEN.fill(BGCOLOR,rect=scorerect)
            scorerect = SCREEN.blit(scorecount.render(),(5,5))
        
            
        # Updates colors of tiles in board.
        for row in mainGrid.grid:
            for tile in row:
                if tile.colored:
                    SCREEN.fill(FLIPTILECOLOR,rect=tile.rect)
                else:
                    SCREEN.fill(DEFTILECOLOR,rect=tile.rect)
        
        # Checks if game is finished.
        if game_won(mainGrid) and not won:
            won = True
            SCREEN.fill(BGCOLOR,rect=scorerect)
            scorerect = SCREEN.blit(scorecount.renderwin(),(5,5))


        pygame.display.update()

if __name__ == "__main__":
    main()
