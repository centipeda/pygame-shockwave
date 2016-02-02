from shockmain import *

BGCOLOR = (255,255,255)

# create window
SCREEN = pygame.display.set_mode((500,500))
pygame.display.set_caption('Shockwave')
SCREEN.fill(BGCOLOR)

# create game grid
mainGrid = create_grid(GRIDSIZE,GRIDSIZE)
assign_rects(mainGrid.grid)
draw_grid(mainGrid.grid,SCREEN)

while True: # main loop

    # quit if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
