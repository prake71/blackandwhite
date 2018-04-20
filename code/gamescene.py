import pygame
import constants
from player import *
from scene import *
from level01 import *
from customscene import *
import titlescene

class GameScene(Scene):
    scr_w = constants.SCREENWIDTH
    scr_h = constants.SCREENHEIGHT
    def __init__(self, levelno):
        super(GameScene, self).__init__()
        # Create the player
        self.player = Player()

        # Create all the levels
        self.level_list = []
        self.level_list.append(Level_01(self.player))

        # Set the current level
        self.current_level_no = 0
        self.current_level = self.level_list[self.current_level_no]

        self.active_sprite_list = pygame.sprite.Group()
        self.player.level = self.current_level

        self.player.rect.x = 0
        self.player.rect.y =  self.scr_h - self.player.rect.height
        self.active_sprite_list.add(self.player)

    def render(self, screen):
        # ALL CODE TO DRAW SHOULD GOg BELOW THIS COMMENT
        self.current_level.draw(screen)
        self.active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    def update(self):
        # Update the player.
        self.active_sprite_list.update()

        # Update items in the level
        self.current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if self.player.rect.right > self.scr_w:
            self.player.rect.right = self.scr_w

        # If the player gets near the left side, shift the world right (+x)
        if self.player.rect.left < 0:
            self.player.rect.left = 0

        if self.player.goal_reached():
            self.exit()

    def exit(self):
        self.manager.go_to(CustomScene("You Won!"))

    def die(self):
        self.manager.go_to(CustomScene("You lose!"))

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self.manager.go_to(titlescene.TitleScene())
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    self.player.go_left()
                if e.key == pygame.K_RIGHT:
                    self.player.go_right()
                if e.key == pygame.K_SPACE:
                    self.player.jump()
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT and self.player.change_x < 0:
                    self.player.stop()
                if e.key == pygame.K_RIGHT and self.player.change_x > 0:
                    self.player.stop()

