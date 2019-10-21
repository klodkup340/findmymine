import pygame
#game.py
#surface = screen	
from grid import Grid
from menuscreen import MenuScreen

width, height = 399, 580
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FindMyMines")

grid = Grid()
menuscreen = MenuScreen()

#grid.set_cell_value(1,1,'x')

grid.print_grid()
running = True
player = 0

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	mouse = pygame.mouse.get_pos()
	xGrid = mouse[0]//64
	yGrid = mouse[1]//64

	if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:	
		#print(pygame.mouse.get_pressed())
		if pygame.mouse.get_pressed()[0]:
				
			print(mouse[0]//64 ,mouse[1]//64)

			grid.get_mouse(xGrid,yGrid,player)
			grid.check_bomb(xGrid,yGrid,player)
			print(grid.moves)
			if grid.switch_player:
				if player == 0:
					player = 1
				else:
					player = 0
				#xpos = int((mouse[0])/64.0)
				#ypos = int((mouse[1])/64.0)
				#boardh[ypos][xpos]=True
			grid.print_grid()
				

screen.fill(0)

grid.drawBoard(screen)

pygame.display.flip()

while 1:
	MenuScreen()






