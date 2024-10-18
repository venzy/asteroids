import pygame
from constants import *

def main():
	print("Starting asteroids!")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Main loop
	while True:
		# Handle quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		# Paint screen
		screen.fill(pygame.Color(0, 0, 0))
		pygame.display.flip()

if __name__ == "__main__":
	main()
