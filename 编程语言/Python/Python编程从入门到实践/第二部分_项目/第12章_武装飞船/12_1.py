import sys
import pygame

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((888, 999))
	bgcolor = (0, 0, 255)
	screen.fill(bgcolor)
	pygame.display.set_caption("Blue Skey")
	while True:
		pygame.display.flip()
		
run_game()
		
