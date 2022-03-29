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
"""in pygame the x and y posititon starts from the top left of the screen"""
init_x = (S_WIDTH - play_width) // 2 
init_y = S_HEIGHT - play_height
score = 0
run = True
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
GRAY = 128, 128, 128
color_list = [BLACK, WHITE, RED, GREEN, GRAY]
font = pygame.font.SysFont('comicsans', 30, True)
block_size = 20
fall_speed = 0.27
fall_time = 0
locked_shape = {}
change_figure = False
"""Screen Definition"""
SCREEN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Tetris")

"""Game Objects"""
clock = pygame.time.Clock()
figure = Forms(5, 0, (random.choice(color_list)))
next_figure = Forms(5, 0, (random.choice(color_list)))
"""Game functions"""

"""will create a list(a) that will have other list(b) in it.
Every list(b) inside the bigger list(a) represent the number of rows.
Every element inside the inside list(b) represent the colluns,
and every element of that list(b) will have a color inside...
witch in that case is black.
  """


def create_grid(locked_shape):
    grid = [[(BLACK) for a in range(10)] for b in range(20)]
    for c in range(len(grid)):
        for d in range(len(grid[c])):
            if (d, c) in locked_shape:
                e = locked_shape[(d, c)]
                grid[c][d] = e
    return grid


def convert_shape(obj1):
    positions = []
    forms = obj1.shape[obj1.rotation % len(obj1.shape)]
    for a, line in enumerate(forms):
        row = list(line)
        for b, collumn in enumerate(row):
            if collumn == "0":
                positions.append((obj1.x + b, obj1.y + a))

    for a, pos in enumerate(positions):
        positions[a] = (pos[0] - 2, pos[1] -4)
    return positions


def check_game_over(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def draw_grid(surface, rows, coll):
    sx = init_x  # draw the lines of the grid
    sy = init_y
    for i in range(rows):  # Horizontal lines
        pygame.draw.line(surface, (GRAY), (sx, sy + i * block_size),
        (sx + play_width, sy + i * block_size))
        for j in range(coll):  # Vertical lines
            pygame.draw.line(surface, (GRAY), (sx + j * block_size, sy),
            (sx + j * block_size, sy + play_height))


def get_form(obj):
    obj.get_shape()
    current_form = obj.shape
    return current_form


def valid_area(obj, grid):
    accepted_positions = [[(a, b) for a in range(10) if grid[b][a] == (BLACK)]for
    b in range(20)]
    accepted_positions = [a for sub in accepted_positions for a in sub]
    final_figure = convert_shape(figure)
    for pos in final_figure:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True


def pop_line():
    pass


def game_fonts():
    text = font.render('Score: ' + str(score), 1, (GREEN))
    SCREEN.blit(text, (8, 10))
    title = font.render('Tetris', 1, (WHITE))
    SCREEN.blit(title, (250, 100))


"""object action"""
grid = create_grid(locked_shape)
get_form(figure)
get_form(next_figure)

"""Game loop"""
while run:
    for event in pygame.event.get():  # event catcher for inputs
        if event.type == QUIT:
            pygame.quit()  # close the game if you click on the x button
    if event.type == pygame.KEYDOWN:  # keypress event
        if event.key == K_UP:  # Rotate the figure
            figure.rotation = figure.rotation + 1 % len(figure.shape)
            if not valid_area(figure, grid):
                figure.rotation = figure.rotation - 1 % len(figure.shape)

        if event.key == K_DOWN:  # accelerate fall
            figure.y += 1
            if not valid_area(figure, grid):
                figure.y -= 1

        if event.key == K_LEFT:
            figure.x -= 1
            if not valid_area(figure, grid):
                figure.x += 1

        if event.key == _RIGHT:
            figure.x += 1
            if not valid_area(figure, grid):
                figure.x -= 1

    fall_time += clock.get_rawtime()
    clock.tick()
    #  Figure falling
    if fall_time / 1000 >= fall_speed:
        fall_time = 0
        figure.y += 1
        if not (valid_area(figure, grid)) and figure.y > 0:
            figure.y -= 1
            change_figure = True
    figure_pos = convert_shape(figure)

    for a in range(len(figure_pos)):  # adding color to the figure
        x, y = figure_pos[a]
        if y > -1:
            grid[y][x] = figure.color

    if change_figure:  # when figure hit the ground
        for pos in figure_pos:
            p = (pos[0], pos[1])
            locked_shape[p] = figure.color
        figure = next_figure
        next_figure = Forms(5, 0, (random.choice(color_list)))
        get_form(next_figure)
        change_figure = False

    if check_game_over(locked_shape):
        run = False

    """SCREEN action"""
    SCREEN.fill(BLACK)
    draw_grid(SCREEN, 20, 10)
    pygame.draw.rect(SCREEN, ((RED)), (init_x, init_y, play_width, play_height), 4)
    pygame.display.update()
    game_fonts()
    draw_grid(SCREEN,20, 10)
    pygame.display.update()
