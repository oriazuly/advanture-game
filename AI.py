from Constants import *
from Tiles import *


def AI_movement(map, tiles, character):
    row = 0
    col = 0
    if character.onGround():
        for i in range(5):
            for j in range(SHELF_HEIGHT_DIFF * 2):
                if 0 < j < MAP_COLS:
                    if tiles[i][j]. == "R":
                        row = i
                        col = j
                        break

        for i in range(JUMP + JUMP - )