import pygame
from grid import Grid
import socket	
import threading
from menuscreen import MenuScreen

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
connection_established = False
conn, addr = None, None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen()

def receieve_data():
	global turn
	while True:
		data = conn.recv(1024).decode()
		data = data.split('-') #split received data with dash
		#xGrid-yGrid-yourturn-PLaying
		x,y = int(data[0]) , int(data[1])
		if data[2] == 'yourturn': #if it is your turn then turn is true
			turn = True
		if data[3] == 'False':
			grid.game_over = True 
		if grid.get_cell_value(x,y) == False:
			grid.set_cell_value(x,y,True)
		print(data)

def waiting_for_connection(): 
	global connection_established, conn, addr
	conn,addr = sock.accept() #Wait for connection, it is a blocking method
	print('Client is connected')
	connection_established = True
	receieve_data()

create_thread(waiting_for_connection)



grid = Grid()
#menuscreen = MenuScreen()
#grid.set_cell_value(1,1,'x')


running = True
player = 0
turn = True
playing = "True"

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN and connection_established:	#not grid.game_over
			#print(pygame.mouse.get_pressed())
			if pygame.mouse.get_pressed()[0]:
				if turn and not grid.game_over:
					mouse = pygame.mouse.get_pos()
					print(mouse[0]//64 ,mouse[1]//64)
					xGrid = mouse[0]//64
					yGrid = mouse[1]//64
					grid.get_mouse(xGrid,yGrid,player)
					grid.check_bomb(xGrid,yGrid,player)

					send_data = '{}-{}-{}-{}'.format(xGrid,yGrid,'yourturn', playing).encode() #this returns string #send data to socket
					conn.send(send_data) #conn object is create when client is connected
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






