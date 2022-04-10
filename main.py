import pygame
from Constants import *
from Functions import *
from Characters.Character import *
from Characters.BasicCharacter import *
from Characters.ReversedCharacter import *
from Furniture import *
from Camera import *

pygame.init()
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.draw.rect(screen, color, pygame.Rect(x_pos, y_pos, width, height))
pygame.display.flip()


text = ""


def beginner():
    create_shelves(10, tiles, 6, "R", 1, int(MAP_COLS // 2))
    return "This is the easier level"


def advanced():
    create_shelves(10, tiles, 4, "R", 1, int(MAP_COLS // 2))
    return "This is the advance level good luck my friend"


def hard_level():
    create_shelves(10, tiles, 2, "R", 1, int(MAP_COLS // 2))
    return "Impossible level you are insane?!"



pygame.init()
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Adventure_game")
pygame.display.flip()

write_map("map.txt", MAP_ROWS, MAP_COLS)
map = generate_map(MAP_ROWS, MAP_COLS)
map = read_map()
tiles = generate_tiles(map)

# create_desk(tiles, 3, MAP_ROWS - 12, "G", 10, FLOOR_HEIGHT)
# create_chandeliers(30, 20, tiles, "M", "Y", 40, CELLING_HEIGHT)
# create_low_chandelier(tiles, "M", "Y", 4, CELLING_HEIGHT)
# create_border(tiles, 5, 5, "X", 4, FLOOR_HEIGHT)

character_src = pygame.image.load("Characters/Character\\cube.png")  # / - Folder, \\ - File
character_src = pygame.transform.scale(character_src, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
character = BasicCharacter(character_src, X_POSITION, Y_POSITION)

jumping = False
jump_counter = 0
falling = False
camera_end = CAMERA_X_END
run = True
killed = False
changeable = True
clock = pygame.time.Clock()

# text = beginner()
# text = advanced()
text = hard_level()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():  # close pygame
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if changeable and keys[pygame.K_r]:
        if character.type() == "B":
            character_src = pygame.image.load("Characters/Character\\cubeReversed.png")
            character_src = pygame.transform.scale(character_src, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
            character = ReversedCharacter(character_src, character.getX(), character.getY())

        elif character.type() == "R":
            character_src = pygame.image.load("Characters/Character\\cube.png")
            character_src = pygame.transform.scale(character_src, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
            character = BasicCharacter(character_src, character.getX(), character.getY())
            changeable = False

    # if X_TEXT_POS == 0:
    #     text = beginner()
    # elif X_TEXT_POS == 200:
    #     text = advanced()
    # else:
    #     text = hard_level()



    camera_end, jumping, jump_counter, falling = character.movement(map, tiles, camera_end, jumping, jump_counter, falling)
    if isKilled(tiles, character.getX(), character.getY()):
        kill_character(character)
        tiles = generate_tiles(map)
        draw_map(tiles, screen, (Camera.x, Camera.y))
        beginner()
    if not changeable:
        changeable = character.onGround(tiles)

    Camera.update()
    screen.fill((0, 0, 0))  # Clear the screen, add another layout
    Camera.draw(screen, tiles, character, 300, text)
    pygame.display.update()  # update the screen

pygame.quit()
