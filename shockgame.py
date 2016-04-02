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

    # Limits.
    FPS = 30
    FLIPFRAME = 2
    frame = 0
    fpsClock = pygame.time.Clock()

    # Creating game grid.
    mainGrid = create_grid(GRIDW,GRIDH)
    mainGrid.assign_rects()
    mainGrid.draw_grid(SCREEN)

    # Drawing score counter.
    scorecount = Score()
    scorerect = SCREEN.blit(scorecount.render(),(5,5))

    # For incrementally updating tiles.
    done = {"left":False,
             "right":False,
             "up":False,
             "down":False}
    flipping = False
    dist = 0

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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Checks if there's a tile at the clicked location.
        # If so, flips tiles.
        if (clickCoords is not None) and (flipping == False):
            clickedTile = tile_at_location(mainGrid,clickCoords)
            if clickedTile is not False:
                play_beep()
                flipping = True
                dist = 1
                clrow = clickedTile.gridrow
                clcol = clickedTile.gridcol
                scorecount.count += 1

        # Updates score count on board, or displays victory message.
        if not won:
            SCREEN.fill(BGCOLOR,rect=scorerect)
            scorerect = SCREEN.blit(scorecount.render(),(5,5))
        
        # Incrementally updates tiles.
        if (flipping is True) and (frame % FLIPFRAME == 0):
            if done["left"] is False and (clcol - dist >= 0):
                mainGrid.flip_relative(clrow,clcol,"left",dist)
            else: 
                done["left"] = True
            if done["right"] is False and (clcol + dist < GRIDW):
                mainGrid.flip_relative(clrow,clcol,"right",dist)
            else:
                done["right"] = True
            if done["up"] is False and (clrow - dist >= 0):
                mainGrid.flip_relative(clrow,clcol,"up",dist)
            else:
                done["up"] = True
            if done["down"] is False and (clrow + dist < GRIDH):
                mainGrid.flip_relative(clrow,clcol,"down",dist)
            else:
                done["down"] = True
        
        if set(done.values()) == set([True]): # if all of done is True
            flipping = False
            done["left"] = False
            done["right"] = False
            done["up"] = False
            done["down"] = False
        elif flipping == True and (frame % FLIPFRAME == 0):
            dist += 1

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


        frame += 1
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()
