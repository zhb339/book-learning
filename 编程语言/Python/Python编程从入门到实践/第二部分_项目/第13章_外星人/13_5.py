import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint

class Drop(Sprite):
	def __init__(self, screen):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load("drop.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.rect.x = randint(10, self.screen_rect.width - 10)
		self.rect.y = 0
	def update(self):
		self.rect.y += 1
		self.screen.blit(self.image, self.rect)

class Tablet(Sprite):
	def __init__(self, screen):
		super().__init__()
		self.screen = screen
		self.rect = pygame.Rect(0, 0, 100, 6)
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom - 100
		self.move_left = False
		self.move_right = False
	def blitme(self):
		if (self.move_left == True and self.rect.left > 0):
			self.rect.centerx -= 1
		elif (self.move_right == True and self.rect.right < self.screen_rect.right):
			self.rect.centerx += 1
		pygame.draw.rect(self.screen, (9, 9, 9), self.rect)		

def check_status(screen, drops, tablets):
	pygame.sprite.groupcollide(drops, tablets, True, False)
	if (len(drops) == 0):
		print("Drop 0")
		drop = Drop(screen)
		drops.add(drop)
 

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((666, 555))
	bgcolor = (222, 222, 255)
	screen.fill(bgcolor)
	
	tablet = Tablet(screen)
	tablets = Group()
	tablets.add(tablet)
	
	drop = Drop(screen)
	drops = Group()
	drops.add(drop)
	
	pygame.display.set_caption("Blue Skey")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					tablet.move_left = True
				elif event.key == pygame.K_RIGHT:
					tablet.move_right = True	
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					tablet.move_left = False
				elif event.key == pygame.K_RIGHT:
					tablet.move_right = False	
		screen.fill(bgcolor)			
		tablet.blitme()
		drops.update()
		check_status(screen, drops, tablets)
		for drop in drops.copy():
			if drop.rect.y > screen.get_rect().height:
				drops.remove(drop)
				drop = Drop(screen)
				drops.add(drop)
		
		pygame.display.flip()
		
run_game()
