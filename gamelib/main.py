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
from gamelib.scene import MainScene
from gamelib.sprite import Spritey


def main():
    ''' entry point of the game '''

    pygame.init()
    real_screen = pygame.display.set_mode([640*2, 480*2])

    clock = pygame.time.Clock()

    scene = MainScene()

    while scene:
        scene = scene.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.QUIT:
                scene = None

        if scene:
            scene.draw(real_screen)
            pygame.display.flip()
            clock.tick(60)