import pygame
import constants



class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 15
        height = 15
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.RED)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

        self.inlevelno = 0

        self.goal_reached = False

        # sounds
        pygame.mixer.init()
        self.snd_jump = pygame.mixer.Sound("sounds/SFX_Jump_50.wav")
        self.snd_jump.set_volume(0.01)

    def update(self):
        """ Move the player. """
        # Gravity
        if self.inlevelno == 0:
            self.calc_grav()
        else:
            self.calc_antigrav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        # WORLD 0
        if self.inlevelno == 0:
            self.rect.y += self.change_y
            # Check and see if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:
                # Reset our position based on the top/bottom of the object.
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                # Stop our vertical movement
                self.change_y = 0
        # WORLD 1
        else:
            self.rect.y += self.change_y
            # Check and see if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:
                # Reset our position based on the top/bottom of the object.
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                # Stop our vertical movement
                self.change_y = 0


        if self.goal_reached:
            print ("Goal reached, level completed!")

    def level_completed(self):
        goal_hit_list = pygame.sprite.spritecollide(self, self.level.goal_list, False)
        if len(goal_hit_list) > 0:
            self.goal_reached = True
        else:
            self.goal_reached = False
        return self.goal_reached


    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .40

        # See if we are on the ground.
        if self.rect.y >= constants.SCREENHEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREENHEIGHT - self.rect.height

    def calc_antigrav(self):
        if self.change_y == 0:
            self.change_y = -1
        else:
            self.change_y -= .40

            # See if we are on the ground.
        if self.rect.y <= 0 and self.change_y <= 0:
            self.change_y = 0
            self.rect.y = 0

    def jump(self):
        """ Called when user hits 'jump' button. """
        self.snd_jump.play()
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREENHEIGHT:
            self.change_y = -6

    def jump_mirror(self):
        print("in jump mirror")
        self.snd_jump.play()
        self.rect.bottom -= 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.bottom -= 2
        if len(platform_hit_list) > 0 or self.rect.top <= 0:
            self.change_y = +7


    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -5

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 5

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


