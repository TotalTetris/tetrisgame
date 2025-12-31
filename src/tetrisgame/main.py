# This is the main function for the Tetris game.

import random
import sys

import pygame

from board import Board
from config import SHAPES, COLORS, COLS, ROWS, BLOCK_SIZE, FALL_INTERVAL
BLACK = COLORS[7]

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


class Tetromino:
    def __init__(self, shape, color, board: Board):
        self.shape = shape
        self.color = color
        # center the shape on the board
        self.x = board.cols // 2 - 2
        self.y = -2

    def cells(self):
        return shape_cells(self.shape)

    def move(self, dx, dy, board: Board) -> bool:
        new_x = self.x + dx
        new_y = self.y + dy
        if board.can_place(self.cells(), new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True
        return False

    def rotate(self, board: Board) -> None:
        new_shape = rotate_shape(self.shape)
        if board.can_place(shape_cells(new_shape), self.x, self.y):
            self.shape = new_shape


def next_tetromino(board: Board) -> Tetromino:
    idx = random.randrange(len(SHAPES))
    shape = SHAPES[idx]
    color = COLORS[idx]
    return Tetromino(shape, color, board)


def draw_current_tetromino(surface, tetromino: Tetromino, board: Board):
    """
    Draw the current moving tetromino on the board.
    """
    block = board.block_size
    for x, y in tetromino.cells():
        gx = x + tetromino.x
        gy = y + tetromino.y
        if gy < 0:
            continue
        rect = pygame.Rect(gx * block, gy * block, block, block)
        pygame.draw.rect(surface, tetromino.color, rect)
        pygame.draw.rect(surface, (40, 40, 40), rect, 1)


def main():
    pygame.init()
    cols, rows, block_size = COLS, ROWS, BLOCK_SIZE
    board = Board(cols, rows, block_size)
    screen = pygame.display.set_mode((board.width, board.height))
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()
    fall_interval = FALL_INTERVAL
    fall_timer = 0

    current_tetromino = next_tetromino(board)
    score = 0
    font = pygame.font.SysFont("monospace", 24)
    game_over = False

    while True:
        dt = clock.tick(60)
        fall_timer += dt

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_LEFT:
                    current_tetromino.move(-1, 0, board)
                elif event.key == pygame.K_RIGHT:
                    current_tetromino.move(1, 0, board)
                elif event.key == pygame.K_DOWN:
                    current_tetromino.move(0, 1, board)
                elif event.key == pygame.K_UP:
                    current_tetromino.rotate(board)

        # Automatic falling
        if not game_over and fall_timer >= fall_interval:
            fall_timer = 0
            if not current_tetromino.move(0, 1, board):
                board.lock_piece(
                    current_tetromino.cells(),
                    current_tetromino.x,
                    current_tetromino.y,
                    current_tetromino.color
                )
                cleared = board.clear_lines()
                score += cleared * cleared * 10

                current_tetromino = next_tetromino(board)
                if not board.can_place(current_tetromino.cells(), current_tetromino.x, current_tetromino.y):
                    game_over = True

        # Drawing
        screen.fill(BLACK)
        board.draw(screen)

        if not game_over:
            draw_current_tetromino(screen, current_tetromino, board)

        # Score / game over
        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))

        if game_over:
            game_over_surf = font.render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_surf, (5, 30))

        pygame.display.flip()

        # Quit
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
