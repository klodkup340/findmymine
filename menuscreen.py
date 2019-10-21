import pygame
from pygame.locals import *
#from waitscreen import 
width, height = 399, 580
screen = pygame.display.set_mode((width, height))

class MenuScreen:

	def initGraphics(self):
		self.enternameFont = pygame.font.Font('PressStart2P.ttf', 22)
		self.nameFont = pygame.font.Font('pxlvetica.ttf', 30)
		self.background=pygame.image.load("spaceBG.png")

	def get_key(self):
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				return event.key
			else:
				pass

	def display_box(self, screen, message):

		#font = pygame.font.SysFont("comicsans", 40)
		text = self.enternameFont.render("ENTER YOUR NAME", 1, (255,0,0))

		screen.fill(0)
		screen.blit(self.background, (0,0))
		screen.blit(text, ((399 / 2) - 160, (580 / 2) + 41,))

		pygame.draw.rect(screen, (0,0,0),
					((399 / 2) - 100,
					(580 / 2) + 70,
					200,24), 0)
		pygame.draw.rect(screen, (255,255,255),
					((399 / 2) - 102,
					(580 / 2) + 74,
					204,35), 3)
		if len(message) !=0:
				screen.blit(self.nameFont.render(message, 1, (255,250,205)),
				((399 / 2) - 30, (580 / 2) + 78))

		pygame.display.flip()
		pygame.display.update()

	def __init__(self):

		pygame.init()
		
		self.initGraphics()

		run = True
		clock = pygame.time.Clock()

		current_str = []
		screen.fill(0)
		screen.blit(self.background, (0,0))
		userkey = str(''.join(current_str))
		self.display_box(screen,userkey)
		#self.n = Network()
		#player = int(self.n.getP())

		#game = self.n.send("get")

		while run:
			clock.tick(60)
			inkey = self.get_key()
			if inkey == K_BACKSPACE:
				current_str=[]
				userkey = str(''.join(current_str))
				self.display_box(screen,userkey)
			elif inkey == K_RETURN:
				#enter to start
				self.wait_screen(screen)
			elif inkey <= 127:
				current_str.append(chr(inkey))
				userkey = str(''.join(current_str))
				self.display_box(screen,userkey)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					run = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					run = False
		return userkey

	def wait_screen(self,screen):
		screen.fill((128,128,128))
		self.screen.blit(self.background, (0,0))

		for event in pygame.event.get():
			#quit if the quit button was pressed
			if event.type == pygame.QUIT:
				exit()

		font = pygame.font.SysFont("comicsans", 80)
		text = font.render("Waiting for Player...", 1, (255,0,0), True)
		screen.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))

		pygame.display.update()
