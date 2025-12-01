import pygame
import sys
import random

import Grid
import config

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
COLUMNS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = SCREEN_HEIGHT // BLOCK_SIZE
FPS = 60

# Colors (R, G, B)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Blue
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (128, 0, 128),  # Purple
    (255, 0, 0)     # Red
]

# Tetromino shapes (relative coordinates)
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1],
     [0, 1, 0]],     # T
    [[1, 1, 0],
     [0, 1, 1]],     # S
    [[0, 1, 1],
     [1, 1, 0]],     # Z
    [[1, 1],
     [1, 1]],        # O
    [[1, 1, 1],
     [1, 0, 0]],     # L
    [[1, 1, 1],
     [0, 0, 1]]      # J
]

class Piece:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice(config.COLORS)
        self.x = COLUMNS // 2 - len(shape[0]) // 2
        self.y = 0

    def draw(self, surface):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        surface,
                        self.color,
                        pygame.Rect(
                            (self.x + col_idx) * BLOCK_SIZE,
                            (self.y + row_idx) * BLOCK_SIZE,
                            BLOCK_SIZE,
                            BLOCK_SIZE
                        )
                    )

def main():
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris - Basic Structure")
    clock = pygame.time.Clock()

    # Create first piece
    current_piece = Piece(random.choice(SHAPES))

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Game logic placeholder
        # (Movement, collision, line clearing will go here)

        # Drawing
        screen.fill(BLACK)
        grd = Grid.Grid()
        grd.draw_grid(screen)
        draw_grid(screen)
        current_piece.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
