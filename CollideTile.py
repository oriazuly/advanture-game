import pygame
from Constants import *
from Functions import *
from BasicTile import BasicTile


class CollideTile(BasicTile):
    def __init__(self, img_src, x, y):
        super().__init__(img_src, x, y)

    def isWalkable(self):
        return False
