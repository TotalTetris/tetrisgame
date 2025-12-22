import config
import numpy as np
from position import Position
import pygame as pg


class Block:
    def __init__(self, block_id):
        self.block_id = block_id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = config.Colors.get_cell_colors()

        self.column_offset = 0
        self.row_offset = 0

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def draw(self, screen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pg.Rect(
                tile.column * self.cell_size + 1,
                tile.row * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pg.draw.rect(screen, self.colors[self.block_id], tile_rect)


