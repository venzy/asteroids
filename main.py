import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
	print("Starting asteroids!")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	# New sprites will automatically be added to these containers upon construction
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	# Main loop
	while True:
		# Handle quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		# Update game objects
		for sprite in updatable:
			sprite.update(dt)
		
		# Detect collisions
		for asteroid in asteroids:
			a: CircleShape = asteroid
			if a.colliding(player):
				print("Game over!")
				sys.exit()

		# Paint screen
		screen.fill(pygame.Color(0, 0, 0))
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()

		dt = clock.tick(FRAME_RATE) / 1000

if __name__ == "__main__":
	main()
