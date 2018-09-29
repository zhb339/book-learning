import sys
import pygame



def run_game():
	pygame.init()
	screen = pygame.display.set_mode((666, 555))
	bgcolor = (222, 222, 255)
	screen.fill(bgcolor)
		
	pygame.display.set_caption("Blue Skey")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				print(event.key)
		screen.fill(bgcolor)					
		pygame.display.flip()
		
run_game()
