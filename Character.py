import pygame
from Constants import *
from Functions import *


class Character:
    def __init__(self, img_src, x, y):
        self.img_src = img_src
        self.x = x
        self.y = y

    def movement(self):
        pass

    def getImageSrc(self):
        return self.img_src

    def getX(self):
        return self.x

    def getY(self):
        return self.y
