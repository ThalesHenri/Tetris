import pygame
from pygame.locals import *

pygame.init()
"""Game Var"""
HEIGHT = 600
WIDTH = 600
score = 0
FPS = 10
run = True
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
play_width = 200
play_height = 300
font = pygame.font.SysFont('comicsans', 30, True)
block = 20
"""Screen Definition"""
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

"""Game Objects"""
clock = pygame.time.Clock()

"""Game functions"""


def game_over():
    pass


def draw_grid():
    for x in range(0, play_width, block):
        for y in range(0, play_height, block):
            rect = pygame.Rect((x + play_width), (y + play_height), block, block)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def change_form():
    pass


def pop_figure():
    pass


def show_score():
    text = font.render('Score: ' + str(score), 1, (GREEN))
    SCREEN.blit(text, (8, 10))


"""Game loop"""
while run:
    clock.tick(FPS)
    for event in pygame.event.get():  # event catcher for inputs
        if event.type == QUIT:
            pygame.quit()  # close the game if you click on the x button
    """SCREEN action"""
    SCREEN.fill(BLACK)
    draw_grid()
    show_score()
    pygame.display.update()
