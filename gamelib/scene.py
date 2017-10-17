''' game scenes '''

from gamelib.sprite import Spritey
import pygame


class Scene:
    def __init__(self):
        pass

    def draw(self, real_screen):
        pass

    def update(self):
        return self

class MainScene(Scene):
    def __init__(self):
        self.bg = Spritey('testlevel')
        #self.canvas = pygame.Surface((320,240)).convert()
        self.canvas = pygame.Surface((self.bg.surface.get_width(),self.bg.surface.get_height())).convert()
        self.player = Spritey('player')
        self.square_w = self.player.surface.get_width()
        self.square_h = self.player.surface.get_height()

        self.square_x = 10
        self.square_y = 10

        self.color = (0, 0, 0)
        self.color = (255, 255, 255)
        self.jumptime = 50
        self.ground_collision = False

    def update(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and self.jumptime < 50: 
            self.square_y -= 2
            self.jumptime += 1

        elif self.square_y < self.canvas.get_height()-self.square_h:
            self.square_y +=3
            #square_y = 600-square_h
            if self.square_y >= self.canvas.get_height()-self.square_h:
                self.square_y = self.canvas.get_height()-self.square_h
                self.jumptime = 0
        if pressed[pygame.K_DOWN]: self.square_y += 3
        if pressed[pygame.K_LEFT]: self.square_x -= 3
        if pressed[pygame.K_RIGHT]: self.square_x += 3

        return self
    
    def draw(self, screen):
        #self.canvas.fill((127,127,127))
        self.canvas.blit(self.bg.surface, [0,0])
        rect = pygame.Rect(self.square_x, self.square_y, self.square_h, self.square_w)
        self.canvas.blit(self.player.surface, [self.square_x, self.square_y])
        pygame.transform.scale(self.canvas,(screen.get_width(), screen.get_height()), screen)