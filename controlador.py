import random
import pygame
from pygame.locals import *
from figura import Forms
pygame.init()


"""Game Var"""
S_HEIGHT = 700
S_WIDTH = 600
play_width = 200
play_height = 400
init_x = (S_WIDTH - play_width) // 2
init_y = S_HEIGHT - play_height
score = 0
FPS = 10
run = True
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
GRAY = 128, 128, 128
color_list = [BLACK, WHITE, RED, GREEN, GRAY]
font = pygame.font.SysFont('comicsans', 30, True)
block_size = 20
"""Screen Definition"""
SCREEN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Tetris")

"""Game Objects"""
clock = pygame.time.Clock()

"""Game functions"""

"""will create a list(a) that will have other list(b) in it.
Every list(b) inside the bigger list(a) represent the number of rows.
Every element inside the inside list(b) represent the colluns,
and every element of that list(b) will have a color inside...
witch in that case is black.
  """


def create_grid(locked_shape={}):
    grid = [[(BLACK) for a in range(10)] for b in range(20)]
    for c in range(len(grid)):
        for d in range(len(grid[c])):
            if (d, c) in locked_shape:
                e = locked_shape[(d, c)]
                grid[c][d] = e
    return grid


def convert_shape(shape):
    pass


def game_over():
    pass


def draw_grid(surface, rows, coll):
    sx = init_x  # draw the lines of the grid
    sy = init_y
    for i in range(rows):  # Horizontal lines
        pygame.draw.line(surface, (GRAY), (sx, sy + i * block_size),
        (sx + play_width, sy + i * block_size))
        for j in range(coll):  # Vertical lines
            pygame.draw.line(surface, (GRAY), (sx + j * block_size, sy),
            (sx + j * block_size, sy + play_height))


def get_form():
    obj1 = Forms(5, 0, (random.choice(color_list)))
    obj1.get_shape()
    current_form = obj1.shape
    return current_form




def pop_line():
    pass


def game_fonts():
    text = font.render('Score: ' + str(score), 1, (GREEN))
    SCREEN.blit(text, (8, 10))
    title =  font.render('Tetris', 1, (WHITE))
    SCREEN.blit(title,(250, 100))


"""Game loop"""
while run:
    clock.tick(FPS)
    for event in pygame.event.get():  # event catcher for inputs
        if event.type == QUIT:
            pygame.quit()  # close the game if you click on the x button
    """SCREEN action"""
    SCREEN.fill(BLACK)
    draw_grid(SCREEN, 20, 10)
    pygame.draw.rect(SCREEN, ((RED)), (init_x, init_y, play_width, play_height), 4)
    pygame.display.update()
    game_fonts()
    draw_grid(SCREEN,20, 10)
    get_form()
    pygame.display.update()
