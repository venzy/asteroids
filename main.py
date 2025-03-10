import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	print("Starting asteroids!")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	# Groups to deal with objects in bulk
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# New sprites will automatically be added to these groups upon construction
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

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
		# Note the cast from any is just to help the IDE
		for asteroid_any in asteroids:
			asteroid: CircleShape = asteroid_any
			if asteroid.colliding(player):
				print("Game over!")
				sys.exit()

			for shot_any in shots:
				shot: Shot = shot_any
				if shot.colliding(asteroid):
					asteroid.split()
					shot.kill()

		# Paint screen
		screen.fill(BACKGROUND_COLOR)
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()

		# Single '/' is float division!
		dt = clock.tick(FRAME_RATE) / 1000

if __name__ == "__main__":
	main()
