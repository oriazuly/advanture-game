import pygame
from Constants import *
from Functions import *
from main import screen


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isWalkable(self):
        pass

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y
