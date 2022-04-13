import pygame
from Constants import *
from Functions import *
from Characters.Character import *
from Characters.BasicCharacter import *
from Characters.ReversedCharacter import *
from Furniture import *
from Camera import *

difficulty = 0
text = ""


def beginner():
    create_shelves(10, tiles, 4, "R", 1, int(MAP_COLS // 2))
    return "This is the easier level"


def advanced():
    create_shelves(15, tiles, 3, "R", 1, int(MAP_COLS // 2))
    return "This is the advance level good luck my friend"


def extreme_level():
    create_shelves(10, tiles, 4, "R", 1, int(MAP_COLS // 2))
    return "It's an Impossible level. are you insane?!"


pygame.init()
clock = pygame.time.Clock()
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Adventure_game")
pygame.display.flip()

write_map("map.txt", MAP_ROWS, MAP_COLS)
map = read_map()
tiles = generate_tiles(map)


generate_menu(screen, MENU_COLS, MENU_ROWS)

# create_desk(tiles, 3, MAP_ROWS - 12, "G", 10, FLOOR_HEIGHT)
# create_chandeliers(30, 20, tiles, "M", "Y", 40, CELLING_HEIGHT)
# create_low_chandelier(tiles, "M", "Y", 4, CELLING_HEIGHT)
# create_border(tiles, 5, 5, "X", 4, FLOOR_HEIGHT)


run = True
clicked = False
# screen.fill(random_color_generator())
rects = initiate_menu(screen)

while not clicked:  # Menu screen
    clock.tick(FPS)
    for event in pygame.event.get():  # close pygame
        if event.type == pygame.QUIT:
            clicked = True
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if mouse_in_button(rects[0], mouse_pos):
                text = beginner()
                difficulty = 1
                clicked = True
            elif mouse_in_button(rects[1], mouse_pos):
                text = advanced()
                difficulty = 2
                clicked = True
            elif mouse_in_button(rects[2], mouse_pos):
                text = extreme_level()
                difficulty = 3
                clicked = True


character_src = pygame.image.load("Characters/Character\\cube.png")  # / - Folder, \\ - File
character_src = pygame.transform.scale(character_src, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
character = BasicCharacter(character_src, X_POSITION, Y_POSITION)

jumping = False
jump_counter = 0
falling = False
camera_end = CAMERA_X_END
killed = False
changeable = True
counter = 0

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
            changeable = False

        elif character.type() == "R":
            character_src = pygame.image.load("Characters/Character\\cube.png")
            character_src = pygame.transform.scale(character_src, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
            character = BasicCharacter(character_src, character.getX(), character.getY())
            changeable = False

    camera_end, jumping, jump_counter, falling = character.movement(map, tiles, camera_end, jumping, jump_counter, falling)
    if isKilled(tiles, character.getX(), character.getY()):
        kill_character(character)
        tiles = generate_tiles(map)
        draw_map(tiles, screen, (Camera.x, Camera.y))
        character_src = pygame.image.load("Characters/Character\\cube.png")
        character_src = pygame.transform.scale(character_src, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        character = BasicCharacter(character_src, character.getX(), character.getY())
        changeable = True
        beginner()
    if not changeable:
        changeable = character.onGround(tiles)

    Camera.update()
    screen.fill((0, 0, 0))  # Clear the screen, add another layout
    Camera.draw(screen, tiles, character, text, counter)
    pygame.display.update()  # update the screen
    counter += 1

pygame.quit()
