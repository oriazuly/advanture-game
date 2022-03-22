import pygame
from Constants import *
from Functions import *
from Character import Character


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

        if isWalkable(tiles, self.x + 1, self.y):  # make the character keep moving forward
            if self.x > CAMERA_X_START:
                camera_end -= 1
                if camera_end < 0:  # check if the map get out of the screen
                    if self.x < MAP_ROWS - CAMERA_X_END - 2:  # stop the player at the end
                        self.x += SPEED
                else:
                    for row in range(MAP_ROWS):
                        for col in range(MAP_COLS):
                            destination = tiles[row][col].getX() - SPEED  # make the tiles change location
                            tiles[row][col].setX(destination)
            if self.x <= CAMERA_X_START:  # make the character move in the start to selected destination
                self.x += SPEED

        if isWalkable(tiles, self.x, self.y + 1) and not jumping:  # make the character fall to the ground
            self.y += GRAVITY
            jump_counter = 0
            falling = True

        if not isWalkable(tiles, self.x, self.y + 1):  # turn off the fall system when touched the ground
            falling = False

        return camera_end, jumping, jump_counter, falling
