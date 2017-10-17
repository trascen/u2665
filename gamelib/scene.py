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
        self.canvas = pygame.Surface((640,480)).convert()
        self.player = Spritey('player')
        self.square_w = 90
        self.square_h = 90

        self.square_x = 100
        self.square_y = 100

        self.color = (0, 0, 0)
        self.color = (255, 255, 255)
        self.jumptime = 50
        self.ground_collision = False

    def update(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and self.jumptime < 50: 
            self.square_y -= 2
            self.jumptime += 1

        elif self.square_y < 480-self.square_h:
            self.square_y +=3
            #square_y = 600-square_h
            if self.square_y >= 480-self.square_h:
                self.square_y = 480-self.square_h
                self.jumptime = 0
        if pressed[pygame.K_DOWN]: self.square_y += 3
        if pressed[pygame.K_LEFT]: self.square_x -= 3
        if pressed[pygame.K_RIGHT]: self.square_x += 3

        return self
    
    def draw(self, screen):
        self.canvas.fill((127,127,127))
        rect = pygame.Rect(self.square_x, self.square_y, self.square_h, self.square_w)
        self.canvas.blit(self.player.surface, [self.square_x, self.square_y])
        pygame.transform.scale(self.canvas,(screen.get_width(), screen.get_height()), screen)