import pygame.image

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

MAP_ROWS = 50  # 50
MAP_COLS = 25

SCALE = 20
SPEED = 1
FPS = 4

JUMP = 6
GRAVITY = 1

CHARACTER_HEIGHT = 20
CHARACTER_WIDTH = 20

COLORS = {"B": pygame.image.load("Colors\\blue.png"),
          "Y": pygame.image.load("Colors\\yellow.png"),
          "R": pygame.image.load("Colors\\rust.png"),
          "G": pygame.image.load("Colors\\green.png"),
          "X": pygame.image.load("Colors\\brick_wall.png")}

NOT_WALKABLE = ("X")
