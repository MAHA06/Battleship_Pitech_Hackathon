import pygame
from pygame.locals import *
import square
from square import Square

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

squares = []

s = Square(100, 100)
squares.append(s)

clock = pygame.time.Clock()

# main game loop
while running:

	dt = clock.tick(30)

	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	screen.fill((255, 255, 255))

	for square in squares:
		square.update(dt)

	Square.squares.draw(screen)

	pygame.display.update()

