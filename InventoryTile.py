import pygame
from Constants import *
from Functions import *
from Tile import Tile


class InventoryTile(Tile):
    def __init__(self, inventory_img_src, item_img_src, x, y):
        super().__init__(inventory_img_src, x, y)
        self.img_src = pygame.transform.scale(self.img_src, (INVENTORY_SCALE, INVENTORY_SCALE))
        self.have_value = False

