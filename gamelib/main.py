'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import pygame
import pygame.display
import pygame.surface
import pygame.event
import gamelib.data as data




def main():
    ''' entry point of the game '''

    pygame.init()
    screen = pygame.display.set_mode([800, 600])

    square_w = 90
    square_h = 90

    square_x = 100
    square_y = 100

    color = (0, 0, 0)
    color = (255, 255, 255)

    clock = pygame.time.Clock()

    keep_running = True


    while keep_running:

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: square_y -= 3
        if pressed[pygame.K_DOWN]: square_y += 3
        if pressed[pygame.K_LEFT]: square_x -= 3
        if pressed[pygame.K_RIGHT]: square_x += 3

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.QUIT:
                keep_running = False



        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, color, pygame.Rect(square_x, square_y, square_h, square_w))

        pygame.display.flip()
        clock.tick(60)

        pygame.display.flip()


        print("Hello from your game's main()")
        print(data.load('sample.txt').read())

