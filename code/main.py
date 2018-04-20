import pygame
import constants
from level import *
from level01 import *
from platform import *
from player import *
from scenemanager import *


scr_w = constants.SCREENWIDTH  # screen width
scr_h = constants.SCREENHEIGHT # screen heigth

FPS = 60 #frames per second

def main(args):
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [scr_w, scr_h]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer Jumper")



    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    manager = SceneManager()

    # -------- Main Program Loop -----------
    while not done:
        clock.tick(FPS)

        if pygame.event.get(pygame.QUIT):
            done = False
            return

        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(screen)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        pygame.display.set_caption(str(clock.get_fps()))






    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

