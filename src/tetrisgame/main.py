"""Main function for the Tetris game."""
# TODO: module comments are great, but usually given with """XXX."""

import random
import sys
from typing import Self

import pygame

from board import Board
from config import (
    Colors,
    Text,
    SHAPES,
    COLORS,
    COLS,
    ROWS,
    BLOCK_SIZE,
    GRAY,
    FALL_INTERVAL,
    BLACK,
)


# TODO: star imports are usually considered as bad practice.
# TODO: Import explicit even if it is a bit longer. (PIP 20 - Zen of Python)
#  ruff check complains too


# TODO: this could be a (static) method, as it is only applicable for Tetrominos
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


# TODO: same here
def rotate_shape(shape):
    """
    Rotate a shape 90 degrees clockwise.
    """
    # TODO: optional optimization: store shapes in np.arrays with 0 and 1.
    #  This func would be a `np.rot90()` call
    size = 4
    matrix = [list(row) for row in shape]
    rotated = [["." for _ in range(size)] for _ in range(size)]
    for y in range(size):
        for x in range(size):
            rotated[x][size - y - 1] = matrix[y][x]
    return ["".join(row) for row in rotated]


# TODO: I would mv this class and related functions to a dedicated tetromino module
class Tetromino:
    def __init__(self, shape, color, board: Board):
        """TODO doc."""
        self.shape = shape
        # TODO: isn't the color based on the shape? if you want this to be flexible
        #  just leaf it, otherwise get the color based on the shape
        #  (potential method in `Color` class)
        self.color = color
        # center the shape on the board
        # TODO: this is a great comment!
        self.x = board.cols // 2 - 2
        self.y = -2

    def cells(self):
        """TODO method doc."""
        return shape_cells(self.shape)

    def move(self, dx, dy, board: Board) -> bool:
        """TODO doc."""
        new_x = self.x + dx
        new_y = self.y + dy

        if board.can_place(self.cells(), new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True

        return False

    def rotate(self, board: Board) -> None:
        """TODO doc."""
        new_shape = rotate_shape(self.shape)
        if board.can_place(shape_cells(new_shape), self.x, self.y):
            self.shape = new_shape

    def hard_drop(self, board: Board) -> None:
        """TODO doc."""
        while self.move(0, 1, board):
            pass

    # TODO: good design on the methods!

    @classmethod
    def random(cls, board: Board) -> Self:
        """
        Draw a random Tetromino.

        This can be used to place the next Tetromino on the board.
        """
        idx = random.randrange(len(SHAPES))
        shape = SHAPES[idx]
        color = COLORS[idx]
        return Tetromino(shape, color, board)


# TODO: this would be a prime example of a class method! See above
def next_tetromino(board: Board) -> Tetromino:
    idx = random.randrange(len(SHAPES))
    shape = SHAPES[idx]
    # TODO: pick color in class init? so that each shape will have the dedicated color
    color = COLORS[idx]
    return Tetromino(shape, color, board)


# TODO: typing for all variables
# TODO: why not a method of the tetromino?
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
        pygame.draw.rect(surface, GRAY, rect, 1)


def main():
    """Initializes and runs the Tetris game"""
    pygame.init()
    # cols, rows, block_size = COLS, ROWS, BLOCK_SIZE TODO: dont unpack, they are const
    board = Board(COLS, ROWS, BLOCK_SIZE)
    screen = pygame.display.set_mode((board.width, board.height))
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()
    fall_interval = FALL_INTERVAL
    font = pygame.font.SysFont("monospace", 24)
    game_over_font = pygame.font.SysFont("monospace", 55, bold=True)

    def reset_game():
        new_board = Board(COLS, ROWS, BLOCK_SIZE)
        # TODO:
        # new_tetromino = next_tetromino(new_board)
        new_tetromino = Tetromino.random(board)
        return new_board, new_tetromino, 0, 0, False

    board, current_tetromino, score, fall_timer, game_over = reset_game()

    # Main game loop handles events and rendering
    while True:
        dt = clock.tick(60)
        fall_timer += dt

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r:
                    board, current_tetromino, score, fall_timer, game_over = (
                        reset_game()
                    )
                # elif not game_over:  TODO unnecessary check
                # TODO: quite some level of nesting/indentation which happens in pygame
                #  quite fast. You could separate logic in a
                #  Tetromino.handle_event(event_key=event.key) function
                # Handles tetromino movement and rotation based on keypresses
                if event.key == pygame.K_LEFT:
                    current_tetromino.move(-1, 0, board)
                elif event.key == pygame.K_RIGHT:
                    current_tetromino.move(1, 0, board)
                elif event.key == pygame.K_DOWN:
                    current_tetromino.move(0, 1, board)
                elif event.key == pygame.K_UP:
                    current_tetromino.rotate(board)
                elif event.key == pygame.K_SPACE:
                    current_tetromino.hard_drop(board)

        # Automatic falling
        if not game_over and fall_timer >= fall_interval:
            fall_timer = 0
            if not current_tetromino.move(0, 1, board):
                board.lock_piece(
                    current_tetromino.cells(),
                    current_tetromino.x,
                    current_tetromino.y,
                    current_tetromino.color,
                )
                cleared = board.clear_lines()
                score += cleared * cleared * 10

                current_tetromino = next_tetromino(board)
                # game over when there are cubes in the top row get occupied
                if not all(board.grid[0][x].is_empty() for x in range(board.cols)):
                    game_over = True

        # Drawing
        screen.fill(BLACK)
        board.draw(screen)

        if not game_over:
            # TODO: something like current_tetromino.draw()? Similar to board.draw()
            draw_current_tetromino(screen, current_tetromino, board)

        # Score / game over
        # TODO: in a bigger game text would get its separate config and will be imported
        #  this would also allow for easier language settings.
        # TODO: use you constants
        score_surf = font.render(
            Text.SCORE_TEMPLATE.format(score=score), True, Colors.WHITE
        )
        screen.blit(score_surf, (10, 10))

        if game_over:
            game_over_surf = game_over_font.render(Text.GAME_OVER, True, Colors.WHITE)
            restart_surf = font.render("Press R to restart", True, (255, 255, 255))
            game_over_rect = game_over_surf.get_rect(center=screen.get_rect().center)
            restart_rect = restart_surf.get_rect(
                center=(game_over_rect.centerx, game_over_rect.bottom + 50)
            )
            screen.blit(game_over_surf, game_over_rect)
            screen.blit(restart_surf, restart_rect)

        pygame.display.flip()

        # Quit TODO: rm you do this already above
        # key = pygame.key.get_pressed()
        # if key[pygame.K_ESCAPE]:
        #     pygame.quit()
        #     sys.exit()


if __name__ == "__main__":
    main()
