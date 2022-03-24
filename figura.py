import pygame
pygame.init()


class Form:
    def __init__(self, x, y, shape, color):
        self.shape = shape
        self.x = x
        self.y = y
        self.color = color
