import pygame
import random
class Grid:
	def initGraphics(self):
		self.basegrid=pygame.image.load("blueplayer.png")
		self.clickgrid=pygame.image.load("greenplayer.png")
		self.clickBomb=pygame.image.load("bomb.png")
	

	#initialize how many grid
	def __init__(self):
		self.boardh = [[False for x in range(6)] for y in range(6)]
		#create boardh = [[False,False,False,False,False,False],[],[],[],[],[]]
		#print(self.boardh)
		position =[]
		self.hasBomb =[[False for x in range(6)] for y in range(6)]
		while len(position) <11:
			i,j = random.randint(0,5), random.randint(0,5)
			if(i,j) not in position:
				position.append((i,j))
				self.hasBomb[i][j] = True
		self.initGraphics()
		self.switch_player = True

	#draw the grid			
	def drawBoard(self,screen):
		for x in range(6):
			for y in range(6):
				#if not self.boardh[y][x]:
				#	self.screen.blit(self.basegrid,[(x)*64+5, (y)*64+5])
				if self.hasBomb[y][x]:
					screen.blit(self.clickBomb,[(x)*64+5, (y)*64+5])
				if not self.boardh[y][x]:
					screen.blit(self.basegrid,[(x)*64+5, (y)*64+5])
	
	def get_cell_value(self,x,y):
		return self.boardh[y][x]

	def set_cell_value(self,x,y,value):
		self.boardh[y][x] = value
		#value should be true or false --> already click?

	def get_mouse(self,x,y,player):
		if self.get_cell_value(x,y) == 0:
			self.switch_player = True
			if player == 0: #player 1
				self.set_cell_value(x,y,"p1")
				#should 0 return false to use in hasBomb?
			elif player == 1: #player2
				self.set_cell_value(x,y,"p2")
		else:
			self.switch_player = False
	
	def check_bomb(self, x ,y , player):
		pass


	def print_grid(self):
		for row in self.boardh:
			print(row)