import pygame as pygame
import pygame.image

# Screen:
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

# Map:
MAP_ROWS = 250  # normal: 250
MAP_COLS = 25  # normal: 25
CELLING_HEIGHT = 1  # use as col
FLOOR_HEIGHT = MAP_COLS - 2  # use as col

# Inventory:
INVENTORY_AREA = 20
INVENTORY_SCALE = 60
INVENTORY_ITEM_SCALE = 40

# Other:
SCALE = 20
SPEED = 3
FPS = 12  # normal: 10

# BasicCharacter:
JUMP = 7  # normal: 6
GRAVITY = 1
X_POSITION = 1
Y_POSITION = MAP_COLS - 2

CHARACTER_HEIGHT = 20
CHARACTER_WIDTH = 20

# Camera:
CAMERA_X_START = ((SCREEN_WIDTH - 2) // SCALE) // 3
CAMERA_X_END = MAP_ROWS - SCREEN_WIDTH // SCALE

# Chandler:

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

#               "MCABB": pygame.image.load("Colors\\cabblestone_block.png"),
#               "COLE": pygame.image.load("Colors\\cole_block.png"),
#               "GRASS": pygame.image.load("Colors\\grass_block.png"),
#               "IRON": pygame.image.load("Colors\\iron_block.png"),
#               "MOISTY": pygame.image.load("Colors\\moisty_block.png"),
#               "TNT": pygame.image.load("Colors\\tnt_block.png"),
#               "N": pygame.image.load("House_colors\\normal.png"),
#               "T": pygame.image.load("House_colors\\top.png")
