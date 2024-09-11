import pygame
from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        # inherit from the CircleShape class
        super().__init__(x, y, PLAYER_RADIUS)

        # set the player's position and rotation
        self.position = pygame.Vector2(x, y)
        self.rotation = 0

    # it's came solved
    def triangle(self):
        """
        Return the vertices of the player's triangle.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        Draw the player on the screen.
        """
        # polygon(surface, color, points, width)
        # draw the player's triangle
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
        
    def rotate(self, dt):
        """
        Rotate the player based on the time elapsed.
        """
        # Update the player's rotation angle by adding the product of the turn speed and the elapsed time
        self.rotation += PLAYER_TURN_SPEED * dt

    #method to update the player's position        
    def update(self, dt):
        """
        Update the player based on the time elapsed.
        """
        # return list of all pressed keys boolean values
        keys = pygame.key.get_pressed()

        # if the key is pressed, rotate the player
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # if the key is pressed, move the player
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)


    def move(self, dt):
        """
        Move the player based on the time elapsed.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt