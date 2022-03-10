import pygame
from Constants import *
from Functions import *
from main import screen
from BasicTile import BasicTile


class CollideTile(BasicTile):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def isWalkable(self):
        return False
