import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, ship, screen):
		super().__init__()		
		self.rect = pygame.Rect(0, 0, 12, 6)
		self.rect.centery = ship.rect.centery
		self.rect.centerx = ship.rect.centerx
		self.screen = screen
		self.screen_rect = screen.get_rect()
	def update(self):
		self.rect.centerx += 1
		pygame.draw.rect(self.screen, (66, 9, 9), self.rect)	

class Ship():
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load("ship2.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.left = 0
		self.rect.centery = self.screen_rect.centery
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
	
	bullets = Group()
	
	pygame.display.set_caption("Blue Skey")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					#ship.move_left = True
					pass
				elif event.key == pygame.K_RIGHT:
					#ship.move_right = True	
					pass
				elif event.key == pygame.K_UP:
					ship.move_top = True
				elif event.key == pygame.K_DOWN:
					ship.move_bottom = True
				elif event.key == pygame.K_SPACE:
					bullet = Bullet(ship, screen)
					bullets.add(bullet)
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
		bullets.update()
		for cur_bullet in bullets.copy():
			if (cur_bullet.rect.centerx > cur_bullet.screen_rect.right):
				bullets.remove(cur_bullet)
				print(len(bullets))
		pygame.display.flip()
		
run_game()
