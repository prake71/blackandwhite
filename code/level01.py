import pygame
from level import *
from platform import *
from goal import *

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform

        level = [
            "                                        ",
            "                            --         G",
            "                       --        ----   ",
            "                        ---             ",
            "                               -        ",
            "                             --         ",
            "                        -----           ",
            "                   ----                 ",
            "     -- --      ----                    ",
            " -- -       -------   --                ",
            "                         ---            ",
            "                            --          ",
            "                       --        ----   ",
            "                        ---             ",
            "                               --       ",
            "                             --         ",
            "                        -----           ",
            "                   ----                 ",
            "     -- --      ----                    ",
            " -- -       -------                     ",
            "       -                                ",
            "          -----   ----      --          ",
            "        ---            --        ----   ",
            "               ----     ---             ",
            "                               -        ",
            "                             --         ",
            "                        -----           ",
            "                   ----                 ",
            "     -- --      ----                    ",
            " -- -       -------                     "]

        # Go through the array above and add platforms
        posy = 0
        for line in level:

            posx = 0
            for char in line:
                if char == "-":
                    block = Platform(20, 20)
                    block.rect.x = posx
                    block.rect.y = posy
                    block.player = self.player
                    self.platform_list.add(block)
                if char == "G":
                    goal = Goal(20,20)
                    goal.rect.x = posx
                    goal.rect.y = posy
                    self.goal_list.add(goal)
                posx = posx + 20
            posy = posy + 20
        print(self.platform_list)
