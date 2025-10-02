import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid_pos = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_pos.velocity = pygame.math.Vector2.rotate(self.velocity, split_angle) * 1.2
        asteroid_neg = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_neg.velocity = pygame.math.Vector2.rotate(self.velocity, -split_angle) * 1.2

