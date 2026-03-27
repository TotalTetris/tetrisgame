# This is for creating the game board for the Tetris game.

import pygame

from cubes import Cube
from typing import List, Tuple


class Board:
    """
    The Tetris board build with Cube objects.
    """

    def __init__(self, cols: int = 10, rows: int = 20, block_size: int = 30):
        """
        Initialise a Board.
        :param cols: The number of columns in the board.
        :param rows: The number of rows in the board.
        :param block_size: The size of each block in the board.
        """

        self.cols = cols
        self.rows = rows
        self.block_size = block_size
        self.width = cols * block_size
        self.height = rows * block_size

        # grid[y][x]
        self.grid: List[List[Cube]] = [
            [Cube(x, y, block_size) for x in range(cols)]
            for y in range(rows)
        ]

    def is_inside(self, x: int, y: int) -> bool:
        """Checks if a cube is within the board or outside."""
        return 0 <= x < self.cols and 0 <= y < self.rows

    def is_available(self, x: int, y: int) -> bool:
        """Checks if a space on the board is available for a cube to enter it."""
        if not self.is_inside(x, y):
            return False
        return self.grid[y][x].is_empty()

    def can_place(self, cells: List[Tuple[int, int]], offset_x: int, offset_y: int) -> bool:
        """
        Checks if a piece with given local cells can be placed at (offset_x, offset_y).
        Cells is a list of (x, y) in tetromino-local coordinates (0..3).
        :param cells: The cells of the board.
        :param offset_x: The offset of the cube in the x coordinate.
        :param offset_y: The offset of the cube in the y coordinate.
        :return: True
        """
        for x, y in cells:
            gx = x + offset_x
            gy = y + offset_y
            if gy < 0:
                continue
            if not self.is_inside(gx, gy):
                return False
            if not self.is_available(gx, gy):
                return False
        return True

    def lock_piece(self, cells, offset_x: int, offset_y: int, color) -> None:
        """
        Permanently place a piece onto the board.
        :param cells: The cells of the grid.
        :param offset_x: The offset of the cube in the x coordinate.
        :param offset_y: The offset of the cube in the y coordinate.
        :param color: The color of the cube.
        :return: None
        """
        for x, y in cells:
            gx = x + offset_x
            gy = y + offset_y
            if self.is_inside(gx, gy):
                cube = self.grid[gy][gx]
                cube.set(color, locked=True)

    def clear_lines(self) -> int:
        """
        Clear any full rows. Returns number of cleared lines.
        """
        cleared = 0
        row = self.rows - 1
        while row >= 0:
            if all(not self.grid[row][x].is_empty() for x in range(self.cols)):
                cleared += 1
                # move all rows above down
                for move_row in range(row, 0, -1):
                    for x in range(self.cols):
                        above = self.grid[move_row - 1][x]
                        self.grid[move_row][x].color = above.color
                        self.grid[move_row][x].locked = above.locked
                # clear the top row
                for x in range(self.cols):
                    self.grid[0][x].clear()
                # re-check the same row index after collapsing
            else:
                row -= 1
        return cleared

    def draw(self, surface: pygame.Surface | pygame.SurfaceType) -> None:
        """
        Draw the cube onto the pygame surface.
        :param surface: The pygame surface on which to draw the cube on.
        :return:
        """
        for row in self.grid:
            for cube in row:
                cube.draw(surface)