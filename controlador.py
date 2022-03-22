import pygame
from pygame.locals import *

pygame.init()
"""Game Var"""
HEIGHT = 600
WIDTH = 400
score = 0
FPS = 10
run = True
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
font = pygame.font.SysFont('comicsans', 30, True)
"""Screen Definition"""
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

"""Game Objects"""
clock = pygame.time.Clock()

"""Game functions"""


def draw_grid():
    block = 20
    for x in range(0, WIDTH, block):
        for y in range(0, HEIGHT, block):
            rect = pygame.Rect(x, y, block, block)
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
