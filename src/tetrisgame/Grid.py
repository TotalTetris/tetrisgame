# Creates the game grid.

# Imports.
import config
import numpy as np
import pygame as pg



# Create the grid.
class Grid:
    """Creates and draws the playing grid"""

    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = np.zeros((20, 10))

    def draw_grid(self):
        """Draws the playing grid"""
        pass

    def get_cell_colours(self, colour_num: int):
        colours = {
            1: (0, 255, 255),  # Cyan
        }
        return colours[colour_num]

    def draw_grid(self, surface):
        for x in range(0, config.SCREEN_WIDTH, config.BLOCK_SIZE):
            pg.draw.line(surface, config.GRAY, (x, 0), (x, config.SCREEN_HEIGHT))
        for y in range(0, config.SCREEN_HEIGHT, config.BLOCK_SIZE):
            pg.draw.line(surface, config.GRAY, (0, y), (config.SCREEN_WIDTH, y))



