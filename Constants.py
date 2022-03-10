import pygame.image

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

MAP_ROWS = 50  # 50
MAP_COLS = 25
ALL_TILES = MAP_COLS * MAP_ROWS

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

ALL_COLORS = {"B": pygame.image.load("Colors\\blue.png"),
              "Y": pygame.image.load("Colors\\yellow.png"),
              "R": pygame.image.load("Colors\\rust.png"),
              "G": pygame.image.load("Colors\\green.png"),
              "X": pygame.image.load("Colors\\brick_wall.png")}

BASIC_COLORS = {"B": pygame.image.load("Colors\\blue.png"),
                "Y": pygame.image.load("Colors\\yellow.png"),
                "R": pygame.image.load("Colors\\rust.png"),
                "G": pygame.image.load("Colors\\green.png")}

COLLIDER_COLORS = {"X": pygame.image.load("Colors\\brick_wall.png")}
