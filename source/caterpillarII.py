#!/usr/bin/env python3
"""An online refactoring of the game 'Caterpillar' using PyGame."""

from player import Player
from settings import Settings
import pygame
import sys
from network import Network
from leaf import Leaf

__version__ = 2.0


class CaterpillarII:
    """Overall class to manage game."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        self.gamearea = pygame.rect.Rect(
            10, 10, self.settings.screen_width, self.settings.screen_height)

        self.n = Network()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height),
            pygame.RESIZABLE)

        pygame.display.set_caption("CATERPILLAR-II")

        self.p = self.n.getP()
        self.l = Leaf()
        self.clock = pygame.time.Clock()

    def rungame(self):
        """Start the game."""
        while True:
            self.p2 = self.n.send(self.p)

            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try:
                        self.p.reset()
                        self.p.blitme(self.screen)
                    except Exception as e:
                        print(e)
                    return self.p.score
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.p.turn(270)
                    elif event.key == pygame.K_a:
                        self.p.turn(180)
                    elif event.key == pygame.K_s:
                        self.p.turn(90)
                    elif event.key == pygame.K_d:
                        self.p.turn(0)

            if self.p.rect.colliderect(self.l):
                self.l.place()
                self.p.score += 5
                self.p.elongate(10)
                self.p.speed += 1

            if not self.gamearea.contains(self.p):
                self.p.reset()
                self.p.blitme(self.screen)
                break

            self.screen.fill(self.settings.bg_color)
            self.p.update()
            self.p2.update()
            self.p.blitme(self.screen)
            self.p2.blitme(self.screen)
            self.l.blitme(self.screen)

            pygame.display.flip()

        return self.p.score


if __name__ == '__main__':
    game = CaterpillarII()
    try:
        print(game.rungame())
    except Exception as e:
        print(e)
