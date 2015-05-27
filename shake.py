import pygame
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((800,800))
running=True
posx=0
posy=0
c=pygame.time.Clock()
bile=pygame.Sprite.Group()
class bila(pygame.sprite.Sprite)
	squares = pygame.sprite.Group()
	def __init__(self,posx,posy,l)
		bila.squares.add(self)
		self.image = pygame.Surface([l,ll])
		self.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
		self.rect = self.image.get_rect()
		self.rect.x = posx
		self.rect.y = posy

		
	def dese(self):
		for i in b:
			if i="1"





while running:	
	dt=c.tick(24)
	for event in pygame.event.get():
			if event.type==QUIT:
					running=False


