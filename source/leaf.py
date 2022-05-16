#!/usr/bin/env python3
"""A file containing the Leaf class."""

import pygame
import random


class Leaf():
    """A leaf class."""

    def __init__(self):
        """Initialize the leaf."""
        self.rect = pygame.rect.Rect(600, 400, 24, 24)

    def blitme(self, win):
        """Draw self to screen."""
        pygame.draw.rect(win, (0, 255, 0), self.rect)

    def place(self):
        """Place self randomly."""
        self.rect.x = random.randint(60, 1140)
        self.rect.y = random.randint(60, 740)
