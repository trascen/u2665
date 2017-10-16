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

    keep_running = True

    while keep_running:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.QUIT:
            keep_running = False



    print("Hello from your game's main()")
    print(data.load('sample.txt').read())
