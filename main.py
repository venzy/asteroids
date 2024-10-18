import pygame
from constants import *
from player import *

def main():
	print("Starting asteroids!")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# Main loop
	while True:
		# Handle quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		# Update game objects
		player.update(dt)
		
		# Paint screen
		screen.fill(pygame.Color(0, 0, 0))
		player.draw(screen)
		pygame.display.flip()

		dt = clock.tick(FRAME_RATE) / 1000

if __name__ == "__main__":
	main()
