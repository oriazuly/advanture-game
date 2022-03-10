import pygame.transform
import Constants
from CollideTile import CollideTile
from BasicTile import BasicTile
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
    for row in map:
        for col in map[row]:
            for color in Constants.BASIC_COLORS:
                if map[row][col] == color:
                    BasicTile(color, row, col)

            for color in Constants.COLLIDER_COLORS:
                if map[row][col] == color:
                    CollideTile(color, row, col)



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


def draw_map(map, screen):
    for row in range(len(map)):
        for col in range(len(map[row])):
            tile = Constants.ALL_COLORS[map[row][col]]
            pygame.transform.scale(tile, (20, 20))
            screen.blit(tile, (row * Constants.SCALE, col * Constants.SCALE))


def isWalkable(map, row, col):
    for tile in Constants.NOT_WALKABLE:
        if map[row][col] == tile:
            return False
    return True


def updatePlace(screen, map, col, row):  # if the map not moving
    tile = Constants.ALL_COLORS[map[row][col]]
    pygame.transform.scale(tile, (20, 20))
    screen.blit(tile, (row * Constants.SCALE, col * Constants.SCALE))