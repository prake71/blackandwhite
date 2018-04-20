import pygame
import ptext

import constants
from gamescene import *
#from constants import DATADIR


class Background(pygame.sprite.Sprite):
        # -- Methods
        def __init__(self, color, direction):
            # Call the parent's constructor
            super().__init__()

            width = 15
            height = 15
            self.image = pygame.Surface((constants.SCREENWIDTH // 2, constants.SCREENHEIGHT))
            self.image.fill(color)
            self.direction = direction
            # Set a referance to the image rect.
            self.rect = self.image.get_rect()

            if direction > 0:
                self.rect.right = 0
            else:
                self.rect.left = constants.SCREENWIDTH

            # Set speed vector of background
            self.change_x = 0
            self.change_y = 0

            self.delay = 0

        def update(self):
            self.delay -= 1
            if self.delay < 0:
                self.rect.x += 1 * self.direction + self.change_x
                self.delay = 0

            print(self.rect.x)
            self.__check_bounds()

        def __check_bounds(self):
            if self.direction == 1:
                if self.rect.right > constants.SCREENWIDTH // 2:
                    self.rect.right = constants.SCREENWIDTH // 2
                    self.direction = 0
            elif self.direction == -1:
                if self.rect.left < constants.SCREENWIDTH // 2:
                    self.rect.left = constants.SCREENWIDTH // 2
                    self.direction = 0

        #def move(self, tx, ty):



class TitleScene(object):
    # master the two worlds where
    # Black becomes White, Up becomes Down, Left becomes Right
    # Loud becomes Quiet
    global DATADIR
    def __init__(self):
        super(TitleScene, self).__init__()
        #self.font = pygame.font.SysFont('Arial', 56)
        #self.sfont = pygame.font.SysFont('Arial', 32)

        # black background for one half of the screen
        self.black_bg = Background(constants.BLACK, -1)
        self.white_bg = Background(constants.WHITE, 1)
        #self.black_bg.direction = 1
        self.bg_group = pygame.sprite.Group(self.black_bg, self.white_bg)
        pygame.font.init()

    def render(self, screen):

        # beware: ugly!
        screen.fill((255, 0, 0))
        # Bubblegum_Sans.ttf
        ptext.FONT_NAME_TEMPLATE = "fonts/%s.ttf"
        ptext.draw("Black And White", (300, 200), fontname="Bubblegum",fontsize=60)
        #print(pygame.font.get_fonts())


        self.bg_group.draw(screen)
        #screen.blit(self.white_bg,(0,0))



    def update(self):
        self.bg_group.update()

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.manager.go_to(GameScene(0))


