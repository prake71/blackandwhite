import pygame
import constants
from player import *
from scene import *
from level01 import *
from level03 import *
from level02 import *
from customscene import *
import titlescene

class GameScene(Scene):
    scr_w = constants.SCREENWIDTH
    scr_h = constants.SCREENHEIGHT
    def __init__(self, levelno):
        super(GameScene, self).__init__()
        # Create the player
        self.player = Player()
        self.player.inlevelno = levelno
        # Create all the levels
        self.level_list = []

        self.level_list.append(Level_01(self.player))
        self.level_list.append(Level_03(self.player))



        # Set the current level
        self.current_level_no = levelno
        self.current_level = self.level_list[self.current_level_no]
        self.player.level = self.current_level

        self.active_sprite_list = pygame.sprite.Group()

        self.set_player_pos()

        # music
        pygame.mixer.init()
        self.music = pygame.mixer.music.load("music/jumpandrun.ogg")
        pygame.mixer.music.play(-1)


    def set_player_pos(self):
        if self.current_level_no == 0:
            self.player.rect.x = 0
            self.player.rect.y = self.scr_h - self.player.rect.height
            self.active_sprite_list.add(self.player)
        else:
            print("in player mirror")
            self.player.rect.x = constants.SCREENWIDTH - 20
            self.player.rect.y = 0
            self.active_sprite_list.add(self.player)

    def render(self, screen):
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
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

        if self.player.level_completed():
            self.player.goal_reached = False
            self.current_level_no += 1
            if self.current_level_no > len(self.level_list) - 1:
                self.exit()
            else:
                self.current_level = self.level_list[self.current_level_no]
                self.manager.go_to(GameScene(self.current_level_no))

    def exit(self):

        self.manager.go_to(CustomScene("You Won!"))

    def die(self):
        self.manager.go_to(CustomScene("You lose!"))

    def handle_events(self, events):
        if not self.current_level_no % 2:
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
                    if e.key == pygame.K_r:
                        self.set_player_pos()
                    # skip level (for testing)
                    if e.key == pygame.K_s:
                        self.manager.go_to(GameScene(1))
        else:
            for e in events:
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.manager.go_to(titlescene.TitleScene())
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        self.player.go_right()
                    if e.key == pygame.K_RIGHT:
                        self.player.go_left()
                    if e.key == pygame.K_SPACE:
                        self.player.jump_mirror()
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT and self.player.change_x > 0:
                        self.player.stop()
                    if e.key == pygame.K_RIGHT and self.player.change_x < 0:
                        self.player.stop()
                    if e.key == pygame.K_r:
                        self.set_player_pos()

            #self.current_level.check_keys()
