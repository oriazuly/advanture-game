import pygame
from Constants import *
from Functions import *
from Tile import Tile


class BasicTile(Tile):
    def __init__(self, img_src, x, y):
        super().__init__(x, y)
        self.img_src = img_src
        self.img_src = pygame.transform.scale(self.img_src, (SCALE, SCALE))

    def isWalkable(self):
        return True

    def getImgSrc(self):
        return self.img_src

    def setImgSrc(self, img_src):
        self.img_src = img_src
