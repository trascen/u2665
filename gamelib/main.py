'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import pygame
import pygame.display
import pygame.surface
import pygame.event
import pygame.image
import pygame.transform
import gamelib.data as data

class Spritey():
    def __init__(self, name):
        self.surface = pygame.image.load(data.load(name + '.png')).convert()


def main():
    ''' entry point of the game '''


    pygame.init()
    real_screen = pygame.display.set_mode([640*4, 480*4])

    screen = pygame.Surface((640,480)).convert()

    player = Spritey('player')
    square_w = 90
    square_h = 90

    square_x = 100
    square_y = 100

    color = (0, 0, 0)
    color = (255, 255, 255)

    clock = pygame.time.Clock()
    jumptime = 50

    keep_running = True

    ground_collision = False # use for jumping when there are more sprites

    while keep_running:

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and jumptime < 50: 
            square_y -= 2
            jumptime += 1

        elif square_y < 480-square_h:
            square_y +=3
            #square_y = 600-square_h
            if square_y >= 480-square_h:
                square_y = 480-square_h
                jumptime = 0
        if pressed[pygame.K_DOWN]: square_y += 3
        if pressed[pygame.K_LEFT]: square_x -= 3
        if pressed[pygame.K_RIGHT]: square_x += 3

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.QUIT:
                keep_running = False



        screen.fill((127,127,127))
        rect = pygame.Rect(square_x, square_y, square_h, square_w)
        screen.blit(player.surface, [square_x, square_y])

        pygame.transform.scale(screen,(real_screen.get_width(), real_screen.get_height()), real_screen)

        pygame.display.flip()
        clock.tick(60)
        #print(clock.get_fps())




