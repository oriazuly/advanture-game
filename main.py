import pygame
from Constants import *
from Functions import *
from Characters.Character import *
from Characters.BasicCharacter import *
from Characters.ReversedCharacter import *
from Furniture import *
from Camera import *

text = ""
def beginner():
    return "This is the easier level"

def advanced():
    pass

def hard_level():
    pass


pygame.init()
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Adventure_game")
pygame.display.flip()

# write_map("map.txt", MAP_ROWS, MAP_COLS)
map = generate_map(MAP_ROWS, MAP_COLS)
map = read_map()
tiles = generate_tiles(map)
# create_desk(tiles, 3, MAP_ROWS - 12, "G", 10, FLOOR_HEIGHT)
create_chandeliers(30, 20, tiles, "M", "Y", 40, CELLING_HEIGHT)
create_low_chandelier(tiles, "M", "Y", 4, CELLING_HEIGHT)

create_border(tiles, 5, 5, "X", 4, FLOOR_HEIGHT)

create_shelves(10, tiles, 4, "R", 1, int(MAP_COLS // 1.5))

character_src = pygame.image.load("Characters/Character\\cube.png")  # / - Folder, \\ - File
character_src = pygame.transform.scale(character_src, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
character = BasicCharacter(character_src, X_POSITION, Y_POSITION)
text = beginner()

jumping = False
jump_counter = 0
falling = False
camera_end = CAMERA_X_END
run = True
killed = False
changeable = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():  # close pygame
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if changeable and keys[pygame.K_r]:
        if character.type() == "B":
            character = ReversedCharacter(character_src, character.getX(), character.getY())
        elif character.type() == "R":
            character = BasicCharacter(character_src, character.getX(), character.getY())
            changeable = False

    camera_end, jumping, jump_counter, falling, changeable = character.movement(map, tiles, camera_end, jumping, jump_counter, falling, changeable)
    if isKilled(tiles, character.getX(), character.getY()):
        kill_character(character)

    Camera.update()
    screen.fill((0, 0, 0))  # Clear the screen, add another layout
    Camera.draw(screen, tiles, character, 300, text)
    pygame.display.update()  # update the screen

pygame.quit()
