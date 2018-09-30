import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint

class Drop(Sprite):
	def __init__(self, screen, x, y):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load("drop.bmp")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	def update(self):
		self.rect.y += 1
		self.screen.blit(self.image, self.rect)

def generate_stars(screen, rain):
	drop = Drop(screen, 0, 0)
	screen_rect = screen.get_rect()
	
	for drop in rain.copy():
		if (drop.rect.y > screen.get_rect().height):
			rain.remove(drop)

	for cnt in range(1, 2):
		rain.add(Drop(screen, randint(0, screen_rect.width - drop.rect.width), 0))
	
def run_game():
	pygame.init()
	screen = pygame.display.set_mode((666, 555))
	bgcolor = (222, 222, 255)
	screen.fill(bgcolor)
	
	rain = Group()
		
	pygame.display.set_caption("Blue Skey")
	
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(bgcolor)
		generate_stars(screen, rain)			
		rain.update()
		pygame.display.flip()
		
run_game()
