import pygame
from Constants import *
from Functions import *
from Characters.Character import Character


class BasicCharacter(Character):  # normal walkable character
    def __init__(self, img_src, x, y):
        super().__init__(img_src, x, y)

    def movement(self, map, tiles, camera_end, jumping, jump_counter, falling):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if isWalkable(tiles, self.x, self.y - JUMP) and not jumping:  # start the jump and avoid double jump
                jumping = True
                jump_counter = JUMP

        if jumping and jump_counter != 0 and not falling:  # while jumping
            self.y -= 1
            jump_counter -= 1
        else:  # no longer jumping
            if jump_counter == 0 or falling:
                jumping = False
                jump_counter = 0

        if isWalkable(tiles, self.actualX, self.y + 1) and not jumping:  # make the character fall to the ground
            self.y += GRAVITY
            jump_counter = 0
            falling = True

        if not isWalkable(tiles, self.actualX, self.y + 1):  # turn off the fall system when touched the ground
            falling = False

        # make the character move forward
        for x in range(self.actualX + 1, self.actualX + 1 + SPEED):
            if not isWalkable(tiles, x, self.y):
                self.actualX = x - 1
                break
        else:
            self.actualX += SPEED
        
        return camera_end, jumping, jump_counter, falling
