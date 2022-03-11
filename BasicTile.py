import pygame
from Constants import *
from Functions import *
from Tile import Tile


class BasicTile(Tile):
    def __init__(self, img_src, x, y):
        super().__init__(img_src, x, y)

    def isWalkable(self):
        return True
