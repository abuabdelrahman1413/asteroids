import pygame
import random
from constants import *
from circleshape import CircleShape
import math


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            velocity1 = velocity1 * 1.2
            velocity2 = velocity2 * 1.2
            asteroid1 = Asteroid(self.position.x, self.position.y,
                                 self.radius / 2)
            asteroid2 = Asteroid(self.position.x, self.position.y,
                                 self.radius / 2)
            asteroid1.velocity = velocity1
            asteroid2.velocity = velocity2
            self.kill()
