import config
import pygame, sys
from grid import Grid
from blocks import *

pygame.init()
white = (200, 200, 200)

screen = pygame.display.set_mode((300, 600))  # Display surface
pygame.display.set_caption("Tetris - Main_2")

clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

block = IBlock()
# block.move(5, 3)

i = 0
j = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill(config.WHITE)
        game_grid.draw_grid(screen)
        block.draw(screen)

        pygame.display.update()


        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_DOWN:
        #         if i != 19:
        #             game_grid.add_tetronimo(i, j, 8)
        #             i += 1
        #         else:
        #             i = 19
        #             game_grid.add_tetronimo(i, j, 8)
        #     if event.key == pygame.K_UP:
        #         game_grid.add_tetronimo(i, j, 8)
        #         i -= 1
        #     if event.key == pygame.K_LEFT:
        #         game_grid.add_tetronimo(i, j, 8)
        #         j -= 1
        #     if event.key == pygame.K_RIGHT:
        #         game_grid.add_tetronimo(i, j, 8)
        #         j += 1

        clock.tick(60)

