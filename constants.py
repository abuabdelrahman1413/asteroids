SCREEN_WIDTH = 1280
"""
constants.py

This module contains the constants used in the asteroids game.

Attributes:
	SCREEN_WIDTH (int): The width of the game screen.
	SCREEN_HEIGHT (int): The height of the game screen.
	ASTEROID_MIN_RADIUS (int): The minimum radius of an asteroid.
	ASTEROID_KINDS (int): The number of different kinds of asteroids.
	ASTEROID_SPAWN_RATE (float): The rate at which asteroids spawn in seconds.
	ASTEROID_MAX_RADIUS (int): The maximum radius of an asteroid.
"""
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300