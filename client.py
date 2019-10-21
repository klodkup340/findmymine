import pygame
import math
import random



class FindMyMines():

	def initGraphics(self):
		self.basegrid=pygame.image.load("blueplayer.png")
		self.clickgrid=pygame.image.load("greenplayer.png")
		self.clickBomb=pygame.image.load("bomb.png")
		self.yourTurnGreen=pygame.image.load("greenindicator.png")
		self.yourTurnRed=pygame.image.load("redindicator.png")
		self.score_panel=pygame.image.load("score_panel.png")


	def __init__(self):
		pass
		#1
		pygame.init()
		width, height = 389, 489
		#2
		#initialize the screen
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Boxes")
		#3
		#initialize pygame clock
		self.clock=pygame.time.Clock()

		self.boardh = [[False for x in range(6)] for y in range(6)]
		#initialize the graphics
		position =[]
		self.hasBomb =[[False for x in range(6)] for y in range(6)]
		while len(position) <11:
			i,j = random.randint(0,5), random.randint(0,5)
			if(i,j) not in position:
				position.append((i,j))
				self.hasBomb[i][j] = True
		#self.putBomb()
		self.initGraphics()

	def drawBoard(self):
		for x in range(6):
			for y in range(6):
				#if not self.boardh[y][x]:
				#	self.screen.blit(self.basegrid,[(x)*64+5, (y)*64+5])
				if self.hasBomb[y][x]:
					self.screen.blit(self.clickBomb,[(x)*64+5, (y)*64+5])
				if not self.boardh[y][x]:
					self.screen.blit(self.basegrid,[(x)*64+5, (y)*64+5])
	
				#	self.screen.blit(self.clickBomb,[(x)*64+5, (y)*64+5])

	def update(self):
		#sleep to make the game 60 fps
		self.clock.tick(60)
    	#clear the screen
		self.screen.fill(0)
		#draw the board
		self.drawBoard()

		for event in pygame.event.get():
            #quit if the quit button was pressed
			if event.type == pygame.QUIT:
				exit()
		#controlling the mouth
    	#1
		mouse = pygame.mouse.get_pos()
		#2
		xpos = int((mouse[0])/64.0)
		ypos = int((mouse[1])/64.0)
		#3
		is_horizontal = abs(mouse[1] - ypos*64) 
		#4
		ypos = ypos -1 if mouse[1] - ypos*64 < 0 and not is_horizontal else ypos
		xpos = xpos -1 if mouse[0] - xpos*64 < 0 and is_horizontal else xpos
		#5
		board=self.boardh #if is_horizontal else self.boardv 
		#hasBomb = self.hasBomb
		isoutofbounds=False
		#6
		try: 
			if not board[ypos][xpos]: self.screen.blit(self.clickgrid if is_horizontal else self.clickgrid, [xpos*64+5 if is_horizontal else xpos*64+5, ypos*64+5 if is_horizontal else ypos*64+5])
		except:
			isoutofbounds=True
			pass
		if not isoutofbounds:
			alreadyplaced=board[ypos][xpos]
		else:
			alreadyplaced=False

		#update the screen
		pygame.display.flip()

		if pygame.mouse.get_pressed()[0] and not alreadyplaced and not isoutofbounds:
			self.boardh[ypos][xpos]=True
			#if hasBomb:
	
	
bg=FindMyMines() #__init__ is called right here

while 1:
	bg.update()