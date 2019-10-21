import pygame
from grid import Grid
import socket	
import threading
from menuscreen import MenuScreen

width, height = 399, 580
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FindMyMines")

def create_thread(target):
	thread = threading.Thread(target=target)
	thread.deamon = True
	thread.start()

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 

HOST = IPAddr
PORT = 65432
connection_established = False
conn, addr = None, None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen()

def receive_data():
	pass 


def waiting_for_connection():
	global connection_established, conn ,addr
	conn, addr = sock.accept() # wait for a connection, it is blocking method
	print ('Client is connected')
	connection_established = True
	receive_data()
	
create_thread(waiting_for_connection)



grid = Grid()
#menuscreen = MenuScreen()
#grid.set_cell_value(1,1,'x')


running = True
player = 0

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:	
			#print(pygame.mouse.get_pressed())
			if pygame.mouse.get_pressed()[0]:
				mouse = pygame.mouse.get_pos()
				print(mouse[0]//64 ,mouse[1]//64)
				xGrid = mouse[0]//64
				yGrid = mouse[1]//64
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
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and grid.game_over:
				grid.clear_grid()				
				grid.game_over = False
				

	screen.fill((0,0,0))
	#self.screen.blit(self.background, (0,0))
	grid.drawBoard(screen)

	pygame.display.flip()






