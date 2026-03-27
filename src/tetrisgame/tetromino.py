import random
import pygame

from abc import abstractmethod, ABC
from board import Board
from config import (
    Colors, Shapes
)


class Tetromino:
    def __init__(self, shape, color, board: Board):
        self.shape = shape
        self.color = color
        # center the shape on the board
        self.x = board.cols // 2 - 2
        self.y = -2

    @staticmethod
    def shape_cells(shape):
        """
        Convert a 4x4 shape into a list of (x, y) coordinates for occupied cells.
        """
        cells = []
        for y, row in enumerate(shape):
            for x, ch in enumerate(row):
                if ch == "X":
                    cells.append((x, y))
        return cells

    @staticmethod
    def rotate_shape(shape):
        """
        Rotate a shape 90 degrees clockwise.
        """
        size = 4
        matrix = [list(row) for row in shape]
        rotated = [["." for _ in range(size)] for _ in range(size)]
        for y in range(size):
            for x in range(size):
                rotated[x][size - y - 1] = matrix[y][x]
        return ["".join(row) for row in rotated]

    def cells(self):
        """Convert to x, y coordinates and return the conversion."""
        return self.shape_cells(self.shape)

    def move(self, dx: int, dy: int, board: Board) -> bool:
        """
        Boolean representation of if the block can be moved.
        :param dx: Distance to move the cube in the x direction.
        :param dy: Distance to move the cube in the y direction.
        :param board: The board on which the cube moves.
        :return: bool.
        """
        new_x = self.x + dx
        new_y = self.y + dy

        if board.can_place(self.cells(), new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True

        return False

    def rotate(self, board: Board) -> None:
        """
        Rotates the Tetromino.
        :param board: The board on which the Tetromino is rotated.
        :return: None
        """
        new_shape = self.rotate_shape(self.shape)
        if board.can_place(self.shape_cells(new_shape), self.x, self.y):
            self.shape = new_shape

    def hard_drop(self, board: Board) -> None:
        """Drops the cube to the bottom of the grid."""
        while self.move(0, 1, board):
            pass


class TetronimoFactory:
    """Builds Tetrominos."""

    @staticmethod
    def draw_current_tetromino(surface: pygame.Surface, tetromino: Tetromino, board: Board):
        """
        Draw the current moving tetromino on the board.
        """
        block = board.block_size
        # Draws current tetromino block if in bounds
        for x, y in tetromino.cells():
            gx = x + tetromino.x
            gy = y + tetromino.y
            if gy < 0:
                continue
            rect = pygame.Rect(gx * block, gy * block, block, block)
            pygame.draw.rect(surface, tetromino.color, rect)
            pygame.draw.rect(surface, Colors.GRAY, rect, 1)

    @staticmethod
    def create_next_tetromino(board: Board) -> Tetromino:
        """Creates the next tetromino on the board."""
        idx = random.randrange(len(Shapes.SHAPES))
        shape = Shapes.SHAPES[idx]
        color = Colors.COLORS[idx]
        return Tetromino(shape, color, board)



