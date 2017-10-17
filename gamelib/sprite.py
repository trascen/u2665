''' sprite stuff '''

import pygame
from pygame import Color
import pygame.image
import pygame.mask
import gamelib.data as data

class Spritey:
    def __init__(self, name):
        self.surface = pygame.image.load(data.load(name + '.png')).convert()

class Player(Spritey):
    def __init__(self, name, x, y):
        super().__init__(name)
        self.x = x
        self.y = y

class CollisionMap:
    def __init__(self, name):
        self.free_color = Color(255,255,255)
        self.surface = pygame.image.load(data.load(name + '.png'))
        self.mask = pygame.mask.from_surface(self.surface)

    def is_free(self, pos):
        return self.surface.get_at(pos) == self.free_color

    def get_floor(self, pos):
        while self.is_free(pos):
            pos = (pos[0], pos[1]+1)
        return pos