import pygame
from Constants import *
from Functions import *
from Character import *
from BasicCharacter import *

pygame.init()
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Adventure_game")
pygame.display.flip()

map = generate_map(MAP_ROWS, MAP_COLS)
# map = read_map()
tiles = generate_tiles(map)
# print_map(map)
draw_map(tiles, screen)

character_src = pygame.image.load("Character\\miner.png")
character_src = pygame.transform.scale(character_src, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
character = BasicCharacter(character_src, X_POSITION, Y_POSITION)

jumping = False
jump_counter = 0
falling = False
camera_end = CAMERA_X_END
run = True
killed = False
clock = pygame.time.Clock()
while run and not killed:
    clock.tick(FPS)
    camera_end, jumping, jump_counter, falling = character.movement(map, tiles, camera_end, jumping, jump_counter, falling)
    killed = isKillable(tiles, character.getX(), character.getY())  # check if the character is still alive

    for event in pygame.event.get():  # close pygame
        if event.type == pygame.QUIT:
            run = False

    draw_map(tiles, screen)  # redraw the entire map
    screen.blit(character.getImageSrc(), (character.getX() * SCALE, character.getY() * SCALE))  # redraw the character
    pygame.display.update()  # update the screen
pygame.quit()
