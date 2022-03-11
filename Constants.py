import pygame as pygame
import pygame.image

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

MAP_ROWS = 100  # 50
MAP_COLS = 25
ALL_TILES = MAP_COLS * MAP_ROWS

INVENTORY_AREA = 20
INVENTORY_SCALE = 60
INVENTORY_ITEM_SCALE = 40

SCALE = 20
SPEED = 1
FPS = 10

# BasicCharacter:
JUMP = 6
GRAVITY = 1
X_POSITION = 1
Y_POSITION = MAP_COLS - 2

CHARACTER_HEIGHT = 20
CHARACTER_WIDTH = 20

# Camera:
CAMERA_X_START = ((SCREEN_WIDTH - 2) // SCALE) // 3
CAMERA_X_END = SCREEN_WIDTH // SCALE

ALL_COLORS = {"B": pygame.image.load("Colors\\blue.png"),
              "Y": pygame.image.load("Colors\\yellow.png"),
              "R": pygame.image.load("Colors\\rust.png"),
              "G": pygame.image.load("Colors\\green.png"),
              "X": pygame.image.load("Colors\\brick_wall.png"),
              "MCABB": pygame.image.load("Colors\\cabblestone_block.png"),
              "COLE": pygame.image.load("Colors\\cole_block.png"),
              "GRASS": pygame.image.load("Colors\\grass_block.png"),
              "IRON": pygame.image.load("Colors\\iron_block.png"),
              "MOISTY": pygame.image.load("Colors\\moisty_block.png"),
              "TNT": pygame.image.load("Colors\\tnt_block.png")}

BASIC_COLORS = {"B": pygame.image.load("Colors\\blue.png"),
                "Y": pygame.image.load("Colors\\yellow.png"),
                "R": pygame.image.load("Colors\\rust.png"),
                "G": pygame.image.load("Colors\\green.png"),
                "CABB": pygame.image.load("Colors\\cabblestone_block.png"),
                "COLE": pygame.image.load("Colors\\cole_block.png"),
                "GRASS": pygame.image.load("Colors\\grass_block.png"),
                "IRON": pygame.image.load("Colors\\iron_block.png"),
                "MOISTY": pygame.image.load("Colors\\moisty_block.png"),
                "TNT": pygame.image.load("Colors\\tnt_block.png")}

COLLIDER_COLORS = {"X": pygame.image.load("Colors\\brick_wall.png")}
