import pygame
from pygame.locals import *
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

class Square(pygame.sprite.Sprite):

	squares = pygame.sprite.Group()

	def __init__(self, posx, posy,l,ll):
		pygame.sprite.Sprite.__init__(self)

		Square.squares.add(self)

		self.image = pygame.Surface([l,ll])
		self.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
		self.rect = self.image.get_rect()
		self.rect.x = posx
		self.rect.y = posy
		self.velx = 8
		self.vely = 8
	def update2(self,dt):
		self.rect.x += self.velx
		self.rect.y += self.vely
	

		if pygame.key.get_pressed()[K_d]:
			self.velx+=dt/1.5
		else:
			self.velx/=3
		if pygame.key.get_pressed()[K_a]:
			self.velx-=dt/1.5
		else:
			self.velx/=3





	def update(self, dt):
		

		self.rect.x += self.velx
		self.rect.y += self.vely

		if self.rect.x>pygame.display.get_surface().get_width()-25:
			self.rect.x=pygame.display.get_surface().get_width()-25
			self.velx*=-1
		if self.rect.y<= 0:
			self.rect.y=0
			self.vely*=-1
		if self.rect.x<= 0:
			self.rect.x=0
			self.velx*=-1

			

		'''if self.rect.y > pygame.display.get_surface().get_height() - 50:
			self.rect.y = pygame.display.get_surface().get_height() - 50
			self.vely *= -1'''
	def cioc(self,bara):
		if (self.rect.y+50>=bara.rect.y)&(self.rect.x+50>=bara.rect.x)&((self.rect.x+50)<=(bara.rect.x+100)):
			
			self.vely*=-1




squares = []

s = Square(100, 100,50,50)
squares.append(s)

bara=Square(0,pygame.display.get_surface().get_height()-25,100,50)
squares.append(bara)
bara.velx=0
bara.vely=0
clock = pygame.time.Clock()
ok=True
# main game loop
while running:

	dt = clock.tick(30)

	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	if ok:
		screen.fill((255, 255, 255))

		s.update(dt)
		bara.update2(dt)
		s.cioc(bara)
	if s.rect.y+26>pygame.display.get_surface().get_height():
		screen.fill((255, 255, 255))
		ok=False
		font = pygame.font.Font(None, 36)
		text = font.render("Wrong!", 1, (10, 10, 10))
		textpos = text.get_rect()
		textpos.centerx = screen.get_rect().centerx
		screen.blit(text, textpos)


		

	Square.squares.draw(screen)

	pygame.display.update()
