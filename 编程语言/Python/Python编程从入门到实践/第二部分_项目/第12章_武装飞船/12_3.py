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
		self.move_left = False
		self.move_right = False
		self.move_top = False
		self.move_bottom = False
	def blitme(self):
		if (self.move_left == True and self.rect.left > 0):
			self.rect.centerx -= 1
		elif (self.move_right == True and self.rect.right < self.screen_rect.right):
			self.rect.centerx += 1
		elif (self.move_top == True and self.rect.top > 0):
			self.rect.centery -= 1	
		elif (self.move_bottom == True and self.rect.bottom < self.screen_rect.bottom):
			self.rect.centery += 1	
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
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					ship.move_left = True
				elif event.key == pygame.K_RIGHT:
					ship.move_right = True	
				elif event.key == pygame.K_UP:
					ship.move_top = True
				elif event.key == pygame.K_DOWN:
					ship.move_bottom = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					ship.move_left = False
				elif event.key == pygame.K_RIGHT:
					ship.move_right = False	
				elif event.key == pygame.K_UP:
					ship.move_top = False
				elif event.key == pygame.K_DOWN:
					ship.move_bottom = False
		screen.fill(bgcolor)			
		ship.blitme()
		
		pygame.display.flip()
		
run_game()
