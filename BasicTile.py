import pygame
from Constants import *
from Functions import *
from main import screen
from Tile import Tile


class BasicTile(Tile):
    def __init__(self, color, x, y):
        super().__init__(x, y)
        self.color = color

    def isWalkable(self):
        return True

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
