import pygame
from grid import Grid
from menuscreen import MenuScreen
import socket
import threading

width, height = 399, 580
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FindMyMines")
background = pygame.image.load("spaceBG.png")


def create_thread(target):
	thread = threading.Thread(target=target)
	thread.deamon = True
	thread.start()



hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 

HOST = IPAddr
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))


def receive_data():
	global turn
	while True:
		#1024= byte lenght (can receieve) --> 1Magabyte
		data = sock.recv(1024).decode()
		data = data.split('-')
		x,y = int(data[0]) , int(data[1])
		if data[2] == 'yourturn':
			turn = True
		if data[3] == 'False':
			grid.game_over = True
		if grid.get_cell_value(x,y) == False:
			grid.set_cell_value(x,y,True) 
		print(data)


create_thread(receive_data)




grid = Grid()
#menuscreen = MenuScreen()

#grid.set_cell_value(1,1,'x')


running = True
player = 1
turn = False
playing = "True"

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:	
			#print(pygame.mouse.get_pressed())
			if pygame.mouse.get_pressed()[0]:
				if turn and not grid.game_over:
					mouse = pygame.mouse.get_pos()
					xGrid = mouse[0]//64
					yGrid = mouse[1]//64
					grid.get_mouse(xGrid,yGrid,player)
					grid.check_bomb(xGrid,yGrid,player)

					send_data = '{}-{}-{}-{}'.format(xGrid,yGrid,'yourturn', playing).encode() 
					sock.send(send_data)
					turn = False
				grid.print_grid()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and grid.game_over:
				grid.clear_grid()				
				grid.game_over = False
				

	screen.fill((0,0,0))
	screen.blit(background, (0,0))
	

	grid.drawBoard(screen)

	pygame.display.flip()






