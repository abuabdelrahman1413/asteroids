import pygame
import random
from constants import *
from circleshape import CircleShape
import math


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.angle = random.uniform(20 * (math.pi / 180), 50 * (math.pi / 180))

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
