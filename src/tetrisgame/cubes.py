# This is for creating cubes for the Tetris game.

import pygame

from config import BLACK, GRAY


class Cube:
    """
    A single square on the game board. Used to construct the board.
    Coordinates (x, y) are in board grid units, not pixels.
    """

    def __init__(self, x: int, y: int, size: int, color=BLACK, locked: bool = False):
        """
        Initialise a Cube.
        :param x: The x coordinate position of the cube on the grid.
        :param y: The y coordinate position of the cube on the grid.
        :param size: The size of the cube.
        :param color: The color of the cube.
        :param locked: Determines if the cube is locked in place on the board. Important for collision detection.
        """

        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.locked = locked

    def is_empty(self) -> bool:
        """Defines an empty cube on the board."""
        return self.color == BLACK and not self.locked

    def set(self, color: tuple[int], locked: bool = True) -> None:
        """Set the color of the cube and locks it in place on the board."""
        self.color = color
        self.locked = locked

    def clear(self) -> None:
        """Clears the cube from the board."""
        self.color = BLACK
        self.locked = False

    def draw(self, surface: pygame.Surface, border: bool = True) -> None:
        """Draws cell with optional border if not empty"""
        rect = pygame.Rect(
            self.x * self.size,
            self.y * self.size,
            self.size,
            self.size
        )
        if not self.is_empty():
            pygame.draw.rect(surface, self.color, rect)

        if border:
            pygame.draw.rect(surface, GRAY, rect, 1)
