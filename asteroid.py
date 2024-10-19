import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Otherwise, spawn 2 new smaller asteroids at random angles
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # New asteroids get auto-added to the various groups created in main
        # so no need to hang on to them after creation here.
        new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        # Asteroid A gets to move a bit faster
        new_asteroid_a.velocity = self.velocity.rotate(random_angle) * 1.2

        new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_b.velocity = self.velocity.rotate(-random_angle)