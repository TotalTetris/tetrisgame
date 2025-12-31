# This is for creating cubes for the Tetris game.

import pygame

from config import COLORS
BLACK = COLORS[7]
GRID_COLOR = COLORS[8]


class Cube:
    """
    A single square on the game board.
    Coordinates (x, y) are in board grid units, not pixels.
    """
    def __init__(self, x: int, y: int, size: int, color=BLACK, locked: bool = False):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.locked = locked  # used for collision detection

    def is_empty(self) -> bool:
        return self.color == BLACK and not self.locked

    def set(self, color, locked: bool = True) -> None:
        self.color = color
        self.locked = locked

    def clear(self) -> None:
        self.color = BLACK # Black
        self.locked = False

    def draw(self, surface, border: bool = True) -> None:
        rect = pygame.Rect(
            self.x * self.size,
            self.y * self.size,
            self.size,
            self.size
        )
        if not self.is_empty():
            pygame.draw.rect(surface, self.color, rect)

        if border:
            pygame.draw.rect(surface, GRID_COLOR, rect, 1)
