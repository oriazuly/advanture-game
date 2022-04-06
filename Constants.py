import pygame as pygame
import pygame.image

# Screen:
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

# Map:
MAP_ROWS = 100  # normal: 350, after change use write_map("map.txt", MAP_ROWS, MAP_COLS)
MAP_COLS = 25  # normal: 25, after change use write_map("map.txt", MAP_ROWS, MAP_COLS)
CELLING_HEIGHT = 1  # use as col
FLOOR_HEIGHT = MAP_COLS - 2  # use as col

# levels:
Y_TEXT_POS = FLOOR_HEIGHT - 20
X_TEXT_POS = MAP_ROWS

# Inventory:
INVENTORY_AREA = 20
INVENTORY_SCALE = 60
INVENTORY_ITEM_SCALE = 40

# Other:
SCALE = 20
SPEED = 1
FPS = 13  # normal: 12

# BasicCharacter:
JUMP = 5  # normal: 6
GRAVITY = 1
X_POSITION = 1
Y_POSITION = MAP_COLS - 20

CHARACTER_HEIGHT = 20
CHARACTER_WIDTH = 20

# Camera:
CAMERA_X_START = ((SCREEN_WIDTH - 2) // SCALE) // 3
CAMERA_X_END = MAP_ROWS - SCREEN_WIDTH // SCALE

# Shelf:
SHELF_HEIGHT_DIFF = int(JUMP // 2) + 1

# Tiles:
ALL_COLORS = {"B": pygame.image.load("Colors\\black.png"),
              "BL": pygame.image.load("Colors\\blue.png"),
              "Y": pygame.image.load("Colors\\yellow.png"),
              "R": pygame.image.load("Colors\\rust.png"),
              "G": pygame.image.load("Colors\\gold.png"),
              "W": pygame.image.load("Colors\\white.png"),
              "M": pygame.image.load("Colors\\metal.png"),
              "X": pygame.image.load("Colors\\brick_wall.png")}

BASIC_COLORS = {"B": pygame.image.load("Colors\\black.png"),
                "BL": pygame.image.load("Colors\\blue.png"),
                "Y": pygame.image.load("Colors\\yellow.png"),
                "R": pygame.image.load("Colors\\rust.png"),
                "G": pygame.image.load("Colors\\gold.png"),
                "M": pygame.image.load("Colors\\metal.png"),
                "W": pygame.image.load("Colors\\white.png")}

COLLIDER_COLORS = {"X": pygame.image.load("Colors\\brick_wall.png")}

OBSTACLE_COLORS = {"S": pygame.image.load("Colors\\spears.png")}

#               "MCABB": pygame.image.load("Colors\\cabblestone_block.png"),
#               "COLE": pygame.image.load("Colors\\cole_block.png"),
#               "GRASS": pygame.image.load("Colors\\grass_block.png"),
#               "IRON": pygame.image.load("Colors\\iron_block.png"),
#               "MOISTY": pygame.image.load("Colors\\moisty_block.png"),
#               "TNT": pygame.image.load("Colors\\tnt_block.png"),
#               "N": pygame.image.load("House_colors\\normal.png"),
#               "T": pygame.image.load("House_colors\\top.png")