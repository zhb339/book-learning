import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
	def __init__(self, screen, x, y):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load("star.bmp")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	def update(self):
		self.screen.blit(self.image, self.rect)

def generate_stars(screen, stars):
	star = Star(screen, 0, 0)
	screen_rect = screen.get_rect()

	for cnt in range(1, 9):
		stars.add(Star(screen, randint(0, screen_rect.width - star.rect.width), randint(0, screen_rect.height - star.rect.height)))
	
def run_game():
	pygame.init()
	screen = pygame.display.set_mode((666, 555))
	bgcolor = (222, 222, 255)
	screen.fill(bgcolor)
	
	stars = Group()
		
	pygame.display.set_caption("Blue Skey")
	generate_stars(screen, stars)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(bgcolor)			
		stars.update()
		pygame.display.flip()
		
run_game()
