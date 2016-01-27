"""There isn't going to be much here for a while.

Shockwave is a simple game that is based on flipping tiles in a square grid.
"""

import pygame,sys
pygame.init()

# create window
mainDisplay = pygame.display.set_mode((500,500))
while True: # main loop
    # quit if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()
