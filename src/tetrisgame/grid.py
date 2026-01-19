# Creates the game grid.
import pygame

# Imports.
import config
import pygame as pg


# Create the grid.
class Grid:
    """Creates and draws the playing grid"""

    def __init__(self, columns: int = 10, rows: int = 20, block_size: int = 30):
        self.rows = rows
        self.columns = columns
        self.block_size = block_size
        self.width = columns * block_size
        self.height = rows * block_size
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]
        self.colors = config.Colors.get_cell_colors()

    def draw_grid(self, screen):
        """Draws the playing grid"""
        for row in range(self.rows):
            for column in range(self.columns):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.block_size + 1, row * self.block_size + 1,
                                        self.block_size - 1, self.block_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def print_grid(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.grid[row][column], end=" ")
            print()
