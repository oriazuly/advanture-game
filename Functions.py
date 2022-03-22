import pygame.transform
import Constants
from BasicTile import BasicTile
from CollideTile import CollideTile
from CollideTile import *
from BasicTile import *
import random  # random.randint(1, 10)


def generate_map(rows, cols):  # auto create normal unchangeable map
    map = []
    for row in range(rows):
        new_line = []
        for col in range(cols):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                new_line.append("X")
            else:
                random_value = random.randint(1, 100)
                if random_value < 95:
                    new_line.append("CABB")
                elif 95 < random_value < 97:
                    new_line.append("COLE")
                elif 97 < random_value < 99:
                    new_line.append("IRON")
                else:
                    new_line.append("MOISTY")

        map.append(new_line)
    return map


def generate_tiles(map):  # create the tiles based of the map
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


def write_map(map_name, rows, cols):  # create a basic editable text file with a basic map
    f = open(map_name, "w")
    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                f.write("X ")
            # elif col < 6:
            #     f.write("T ")
            # elif col < 8:
            #     f.write("B ")
            else:
                f.write("W ")
        f.write("\n")
    f.close()  # write_map("map.txt", MAP_ROWS, MAP_COLS)


def read_map():  # read the .txt map and return it
    world = []
    f = open("map.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        world.append(line.split(" "))
    f.close()
    return world


def print_map(map):  # print the map
    for row in range(len(map)):
        for col in range(len(map[row])):
            print(map[row][col], end=", ")
        print()


def draw_map(tiles, screen):  # make the tiles list (based map) apper on the screen
    for row in range(MAP_ROWS):
        for col in range(MAP_COLS):
            tile = tiles[row][col]
            pygame.transform.scale(tile.getImgSrc(), (SCALE, SCALE))
            screen.blit(tile.getImgSrc(), (tile.getX() * Constants.SCALE, tile.getY() * Constants.SCALE))


def generate_inventory(map, screen):
    pass


def isWalkable(tiles, row, col):  # is possible to move through the tile
    return tiles[row][col].isWalkable()


def isKillable(tiles, row, col):  # is touch this tile will kill you
    return tiles[row][col].isKillable()


def updatePlace(screen, map, col, row):  # if the map not moving
    tile = Constants.ALL_COLORS[map[row][col]]
    pygame.transform.scale(tile, (20, 20))
    screen.blit(tile, (row * Constants.SCALE, col * Constants.SCALE))
