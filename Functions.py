import pygame.transform
import Constants
from CollideTile import *
from BasicTile import *
import random  # random.randint(1, 10)


def generate_map(rows, cols):
    map = []
    for row in range(rows):
        new_line = []
        for col in range(cols):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                new_line.append("X")
            else:
                new_line.append("G")
        map.append(new_line)
    return map


def generate_tiles(map):
    tiles = []
    for row in range(Constants.MAP_ROWS):
        new_line = []
        for col in range(Constants.MAP_COLS):
            for color in Constants.BASIC_COLORS:
                if map[row][col] == color:
                    new_line.append(BasicTile(Constants.BASIC_COLORS[color], row, col))

            for color in Constants.COLLIDER_COLORS:
                if map[row][col] == color:
                    new_line.append(CollideTile(Constants.COLLIDER_COLORS[color], row, col))
        tiles.append(new_line)
    return tiles


def write_map(map_name, rows, cols):
    f = open(map_name, "w")
    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                f.write("X ")
            else:
                f.write("G ")
        f.write("\n")


def read_map():
    pass


def print_map(map):
    for row in range(len(map)):
        for col in range(len(map[row])):
            print(map[row][col], end=", ")
        print()


def draw_map(tiles, screen):
    for row in range(MAP_ROWS):
        for col in range(MAP_COLS):
            tile = tiles[row][col]
            pygame.transform.scale(tile.getColor(), (20, 20))
            screen.blit(tile.getColor(), (tile.getX() * Constants.SCALE, tile.getY() * Constants.SCALE))


def isWalkable(tiles, row, col):
    return tiles[row][col].isWalkable()


def updatePlace(screen, map, col, row):  # if the map not moving
    tile = Constants.ALL_COLORS[map[row][col]]
    pygame.transform.scale(tile, (20, 20))
    screen.blit(tile, (row * Constants.SCALE, col * Constants.SCALE))