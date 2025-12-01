# This is for creating cubes for the Tetris game.

import pygame

BLACK = (0, 0, 0)
GRID_COLOR = (40, 40, 40)


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
        self.color = BLACK
        self.locked = False


