import pygame
from Constants import *
from Functions import *


class Item:
    def __init__(self, img_src, x, y):
        self.img_src = img_src
        self.img_src = pygame.transform.scale(self.img_src, (SCALE, SCALE))
        self.x = x
        self.y = y
        self.amount = 0

    def getImgSrc(self):
        return self.img_src

    def setImgSrc(self, img_src):
        self.img_src = img_src

    def haveItem(self):
        return self.amount > 0

    def useItem(self):
        if self.haveItem():
            self.amount -= 1

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y
