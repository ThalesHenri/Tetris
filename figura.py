import random
import pygame
pygame.init()


class Forms:
    def __init__(self, x, y, color, shape):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.rotation = 0  # até 3 rotações
