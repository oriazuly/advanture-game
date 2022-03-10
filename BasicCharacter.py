import pygame
from Constants import *
from Functions import *
from Character import Character


class BasicCharacter(Character):
    def __init__(self, img_src, x, y):
        super().__init__(img_src, x, y)

    def movement(self, map, jumping, jump_counter, falling):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if isWalkable(map, self.x, self.y - JUMP) and not jumping:  # start the jump
                jumping = True
                jump_counter = JUMP

        if jumping and jump_counter != 0 and not falling:  # while jumping
            self.y -= 1
            jump_counter -= 1
        else:
            if jump_counter == 0 or falling:
                jumping = False

        if isWalkable(map, self.x + 1, self.y):  # make the character keep moving forward
            self.x += SPEED

        if isWalkable(map, self.x, self.y + 1) and not jumping:  # make the character fall to the ground
            self.y += GRAVITY
            falling = True

        if not isWalkable(map, self.x, self.y + 1):
            falling = False

        return jumping, jump_counter, falling
