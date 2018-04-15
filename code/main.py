import pygame
from constants import *


scr_w = SCREENWIDTH  # screen width
scr_h = SCREENHEIGHT # screen heigth

FPS = 180 # frames per second



def main(args):
    """ app starts here """
    # first iniitalize mixer
    # to avoid sound latency
    # http://stackoverflow.com/questions/18273722/pygame-sound-delay
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    # initalize pygame objects
    pygame.init()

    # setting up the surface
    screen = pygame.display.set_mode([scr_w, scr_h])
    pygame.display.set_caption("Black And White")

    # game ended by closing window
    done = False

    # clock object for limiting game speed
    clock = pygame.time.Clock()
    """"
    my_game = game.Game(screen, FPS)

    # Game Loop
    while not done:
        # handle events
        done = my_game.handle_events()

        # handle game logic
        my_game.update()

        # draw current frame
        my_game.draw_frame(screen)

        # pause before next frame
        clock.tick(FPS)
        pygame.display.set_caption("fps: %.2f"% (clock.get_fps()))

    # close window and quit
    pygame.quit()
"""
