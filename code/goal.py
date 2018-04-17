import pygame
from constants import *

class Goal(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        #pygame.draw.circle(self.image, BLUE, (10, 10),10)

        self.rect = self.image.get_rect()