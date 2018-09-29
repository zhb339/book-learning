import sys
import pygame

class Ship():
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load("ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	def blitme(self):
		self.screen.blit(self.image, self.rect)

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((666, 555))
	bgcolor = (222, 222, 255)
	screen.fill(bgcolor)
	
	ship = Ship(screen)
	
	pygame.display.set_caption("Blue Skey")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		ship.blitme()
		pygame.display.flip()
		
run_game()
		
