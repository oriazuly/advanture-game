import pygame
from Constants import *
from Functions import *
from Character import *
from BasicCharacter import *
from Furniture import *
from Camera import *

pygame.init()
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Adventure_game")
pygame.display.flip()

map = generate_map(MAP_ROWS, MAP_COLS)
write_map("map.txt", MAP_ROWS, MAP_COLS)
map = read_map()
tiles = generate_tiles(map)
create_desk(tiles, 3, 50, "G", 40, FLOOR_HEIGHT)
create_chandeliers(30, 20, tiles, "M", "Y", 20, CELLING_HEIGHT)

character_src = pygame.image.load("Character\\cube.png")
character_src = pygame.transform.scale(character_src, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
character = BasicCharacter(character_src, X_POSITION, Y_POSITION)


jumping = False
jump_counter = 0
falling = False
camera_end = CAMERA_X_END
run = True
killed = False
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():  # close pygame
        if event.type == pygame.QUIT:
            run = False

    camera_end, jumping, jump_counter, falling = character.movement(map, tiles, camera_end, jumping, jump_counter, falling)
    if isKilled(tiles, character.getX(), character.getY()):
        kill_character(character)

    Camera.update()
    screen.fill((0, 0, 0))  # Clear the screen, add another layout
    Camera.draw(screen, tiles, character)
    pygame.display.update()  # update the screen

pygame.quit()
