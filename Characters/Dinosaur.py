import pygame
from Constants import *
from Functions import *
from Characters.Character import Character
import random
import Camera


dinosaur_moves = {1: "up",
                  2: "down",
                  3: "right",
                  4: "left"}


class Dinosaur(Character):
    def __init__(self, img_src, x, y):
        super().__init__(img_src, x, y)

    def movement(self, map, tiles):
        move = random.randint(1, 4)
        move = dinosaur_moves[move]
        if move == "up" and self.onCeiling(tiles):
            self.y -= SPEED
        elif move == "down" and self.onGround(tiles):
            self.y += SPEED
        elif move == "right" and not self.outOfScreenLeft():
            self.actualX += SPEED
        #elif move == "left" and not self.outOfScreenRight():
        #    self.actualX -= SPEED

        # make the character move forward
        for x in range(self.actualX + 1, self.actualX + 1 + SPEED):
            if not isWalkable(tiles, x, self.y):
                self.actualX = x - 1
                break

    def onGround(self, tiles):
        return not isWalkable(tiles, self.actualX, self.y + 1)

    def onCeiling(self, tiles):
        return not isWalkable(tiles, self.actualX, self.y - 1)

#r    def outOfScreenRight(self):
#        return Camera.x < self.actualX < Camera.x + SCREEN_WIDTH // SCALE

    def outOfScreenLeft(self):
        return self.x < MAP_ROWS - SCREEN_WIDTH // SCALE

    def type(self):
        return "D"

    def reset(self):
        self.x = DINOSAUR_X_POSITION
        self.actualX = DINOSAUR_X_POSITION
        self.y = DINOSAUR_Y_POSITION
