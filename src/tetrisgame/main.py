"""This is the main function for the Tetris game."""

import sys

import pygame

from board import Board
from config import (
    Constants, Colors, Text
)
from tetromino import (
    TetronimoFactory
)


def main():
    """Initializes and runs the Tetris game"""
    pygame.init()
    cols, rows, block_size = Constants.COLS, Constants.ROWS, Constants.BLOCK_SIZE
    board = Board(cols, rows, block_size)
    screen = pygame.display.set_mode((board.width, board.height))
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()
    fall_interval = Constants.FALL_INTERVAL
    font = pygame.font.SysFont("monospace", 24)
    game_over_font = pygame.font.SysFont("monospace", 55, bold=True)

    def reset_game():
        """Restart the game with a new board."""
        new_board = Board(cols, rows, block_size)
        new_tetromino = TetronimoFactory.create_next_tetromino(new_board)
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
                    board, current_tetromino, score, fall_timer, game_over = reset_game()
                elif not game_over:
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
                    current_tetromino.color
                )
                cleared = board.clear_lines()
                score += cleared * cleared * 10

                current_tetromino = TetronimoFactory.create_next_tetromino(board)
                # game over when there are cubes in the top row get occupied
                if not all(board.grid[0][x].is_empty() for x in range(board.cols)):
                    game_over = True

        # Drawing
        screen.fill(Colors.BLACK)
        board.draw(screen)

        if not game_over:
            TetronimoFactory.draw_current_tetromino(screen, current_tetromino, board)

        # Score / game over
        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))

        if game_over:
            game_over_surf = game_over_font.render("Game Over", True, (255, 0, 0))
            restart_surf = font.render("Press R to restart", True, (255, 255, 255))
            game_over_rect = game_over_surf.get_rect(center=screen.get_rect().center)
            restart_rect = restart_surf.get_rect(center=(game_over_rect.centerx, game_over_rect.bottom + 50))
            screen.blit(game_over_surf, game_over_rect)
            screen.blit(restart_surf, restart_rect)

        pygame.display.flip()

        # Quit
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
