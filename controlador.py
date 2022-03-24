import random
import pygame
from pygame.locals import *
from figura import Forms
pygame.init()


"""Game Var"""
S_HEIGHT = 700
S_WIDTH = 600
score = 0
FPS = 10
run = True
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
color_list = [BLACK, WHITE, RED, GREEN]
play_width = 200
play_height = 400
grid_rows = 20
grid_colluns = 10
font = pygame.font.SysFont('comicsans', 30, True)
block_size = 20
"""Screen Definition"""
SCREEN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Tetris")

"""Game Objects"""
clock = pygame.time.Clock()

"""Game functions"""


def create_grid(locked_shape={}):
    grid = [[(BLACK) for a in range(10)] for b in range(20)]
    for c in range(len(grid)):
        for d in range(len(grid[c])):
            pass


def game_over():
    pass


def draw_grid():
    
    """for x in range(0, play_width, block_size):
        for y in range(0, play_height, block_size):
            rect = pygame.Rect((x + play_width), (y + play_height - 100), block_size, block_size)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)"""


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
    draw_grid()
    game_fonts()
    get_form()
    play_area(rect)
    pygame.display.update()
