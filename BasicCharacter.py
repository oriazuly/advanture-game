import pygame

import Constants
from Constants import *
from Functions import *
from Character import Character
from math import ceil


class BasicCharacter(Character):  # normal walkable character
    def __init__(self, img_src, x, y):
        super().__init__(img_src, x, y)
        self.actualX = x
        self.actualY = y

    def movement(self, tiles, world):
        if isWalkable(tiles, self.x, self.y + 1):
            self.x += SPEED

    def jump(self, tiles):
        if isWalkable(tiles, self.x, self.y - 1) and not isWalkable(tiles, self.x, self.y + 1):
            self.y -= SPEED
        elif isWalkable(tiles, self.x, self.y + 1):
            self.y += GRAVITY




    def camera(self, world):
        # CAMERA_X_END
        max_camera_x = int(len(world) - (Constants.SCREEN_WIDTH / Constants.SCALE))
        # camera end
        camera_x = self.x - ceil(round(Constants.SCREEN_WIDTH / Constants.SCALE / 2))

        # if max_camera_y >= camera_y >= 0:
        #     self.camera_pos[1] = camera_y
        # if camera_y < 0:
        #     self.camera_pos[1] = 0
        # else:
        #     self.camera_pos[1] = max_camera_y

        if max_camera_x >= camera_x >= 0:
            self.camera_pos -= SPEED * SCALE
        elif camera_x < 0:
            self.camera_pos = 0
        else:
            self.camera_pos = max_camera_x
