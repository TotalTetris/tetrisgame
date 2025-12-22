import config
import numpy as np
import pygame as pg


class Block:
    def __init__(self, block_id):
        self.block_id = block_id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = config.Colors.get_cell_colors()

    def draw(self, screen):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pg.Rect(
                tile.column * self.cell_size + 1,
                tile.row * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pg.draw.rect(screen, self.colors[self.block_id], tile_rect)


