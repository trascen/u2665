''' sprite stuff '''

import pygame.image
import gamelib.data as data

class Spritey:
    def __init__(self, name):
        self.surface = pygame.image.load(data.load(name + '.png')).convert()
