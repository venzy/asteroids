import pygame
from constants import *

def main():
	print("Starting asteroids!")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	# Main loop
	while True:
		# Handle quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		# Paint screen
		screen.fill(pygame.Color(0, 0, 0))
		pygame.display.flip()

		dt = clock.tick(FRAME_RATE) / 1000

if __name__ == "__main__":
	main()
