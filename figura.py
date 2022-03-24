import random
import pygame
pygame.init()


class Forms:
    def __init__(self, x, y, color):
        self.shape = None
        self.x = x
        self.y = y
        self.color = color
        self.rotation = 0

    def get_shape(self):
        S = [['.....',
            '......',
            '..00..',
            '.00...',
            '.....'],
            ['.....',
            '..0..',
            '..00.',
            '...0.',
            '.....']]

        Z = [['.....',
              '.....',
              '.00..',
              '..00.',
              '.....'],
             ['.....',
              '..0..',
              '.00..',
              '.0...',
              '.....']]

        I = [['..0..',
              '..0..',
              '..0..',
              '..0..',
              '.....'],
             ['.....',
              '0000.',
              '.....',
              '.....',
              '.....']]

        O = [['.....',
              '.....',
              '.00..',
              '.00..',
              '.....']]

        J = [['.....',
              '.0...',
              '.000.',
              '.....',
              '.....'],
             ['.....',
              '..00.',
              '..0..',
              '..0..',
              '.....'],
             ['.....',
              '.....',
              '.000.',
              '...0.',
              '.....'],
             ['.....',
              '..0..',
              '..0..',
              '.00..',
              '.....']]

        L = [['.....',
              '...0.',
              '.000.',
              '.....',
              '.....'],
             ['.....',
              '..0..',
              '..0..',
              '..00.',
              '.....'],
             ['.....',
              '.....',
              '.000.',
              '.0...',
              '.....'],
             ['.....',
              '.00..',
              '..0..',
              '..0..',
              '.....']]

        T = [['.....',
              '..0..',
              '.000.',
              '.....',
              '.....'],
             ['.....',
              '..0..',
              '..00.',
              '..0..',
              '.....'],
             ['.....',
              '.....',
              '.000.',
              '..0..',
              '.....'],
             ['.....',
              '..0..',
              '.00..',
              '..0..',
              '.....']]
        shape_list = [S, Z, I, O, J, L, T]
        self.shape = random.choice(shape_list)
        return self.shape
