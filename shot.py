import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    """
    A class to represent a shot fired by the player.
    """

    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    
    def draw(self, screen):
        """
        Draw the shot on the screen.
        
        Args:
            screen (pygame.Surface): The screen to draw on.
        """
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        """
        Update the shot's position.
        
        Args:
            dt (float): The time elapsed since the last update.
        """
        self.position += self.velocity * dt
