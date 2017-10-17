''' game scenes '''

from gamelib.sprite import Spritey, CollisionMap, Player
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
        self.collision_map = CollisionMap('testlevel_collision_map')
        self.canvas = pygame.Surface((self.bg.surface.get_width(),self.bg.surface.get_height())).convert()
        self.player = Player('player', 10, 10)
        self.square_w = self.player.surface.get_width()
        self.square_h = self.player.surface.get_height()

        self.color = (0, 0, 0)
        self.color = (255, 255, 255)
        self.jumptime = 50
        self.ground_collision = False

    def update(self):
        pressed = pygame.key.get_pressed()


        if pressed[pygame.K_UP] and self.jumptime < 50: 
            self.player.y -= 2
            self.jumptime += 1
        else:
            floor_adjusted = self.collision_map.get_floor((self.player.x, self.player.y))[1] - self.square_h
            self.player.y = min(floor_adjusted, self.player.y + 3)
            if self.player.y == floor_adjusted:
                self.jumptime = 0
        if pressed[pygame.K_LEFT]: self.player.x -= 3
        if pressed[pygame.K_RIGHT]: self.player.x += 3
        if self.player.x < 0:
            self.player.x = 0
        if self.player.x >= self.bg.surface.get_width():
            self.player.x = self.bg.surface.get_width()-1

        return self
    
    def draw(self, screen):
        #self.canvas.fill((127,127,127))
        self.canvas.blit(self.bg.surface, [0,0])
        rect = pygame.Rect(self.player.x, self.player.y, self.square_h, self.square_w)
        self.canvas.blit(self.player.surface, [self.player.x, self.player.y])
        pygame.transform.scale(self.canvas,(screen.get_width(), screen.get_height()), screen)