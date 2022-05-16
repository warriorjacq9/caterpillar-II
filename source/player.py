#!/usr/bin/env python3
"""A file containing the Player class."""

import pygame


class Player:
    """The Player class."""

    def __init__(self, x, y, width, height, color):
        """Initialize the player."""
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.direction = 0
        self.speed = 1

        self.rect.x = x
        self.rect.y = y
        self.score = 0

    def update(self):
        """Move self in appropriate direction."""
        if self.direction == 0:
            self.rect.x += self.speed
        elif self.direction == 180:
            self.rect.x -= self.speed
        elif self.direction == 90:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

    def blitme(self, win):
        """Draw self to screen."""
        pygame.draw.rect(win, self.color, self.rect)

    def turn(self, direction):
        """Turn self in direction."""
        if direction == 0 and self.direction != 180:  # right
            self.rect = pygame.rect.Rect(
                self.rect.x, self.rect.y, self.width, self.height)
            self.direction = 0
        elif direction == 180 and self.direction != 0:  # left
            self.rect = pygame.rect.Rect(
                self.rect.x, self.rect.y, self.width, self.height)
            self.direction = 180
        elif direction == 270 and self.direction != 90:  # up
            self.rect = pygame.rect.Rect(
                self.rect.x, self.rect.y, self.height, self.width)
            self.direction = 270
        elif direction == 90 and self.direction != 270:  # down
            self.rect = pygame.rect.Rect(
                self.rect.x, self.rect.y, self.height, self.width)
            self.direction = 90

    def elongate(self, y):
        """Make caterpillar y pixels longer."""
        direction = self.direction
        self.turn(0)
        self.width += y
        self.rect = pygame.rect.Rect(
            self.rect.x, self.rect.y, self.width, self.height)
        self.turn(direction)

    def reset(self):
        """Reset self."""
        self.score = 0
        self.direction = 0
        self.speed = 1
