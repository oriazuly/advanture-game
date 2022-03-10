import pygame
from Constants import *
from Functions import *
pygame.init()
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.flip()

map = generate_map(MAP_ROWS, MAP_COLS)
print_map(map)
draw_map(map, screen)
write_map("map.txt", MAP_ROWS, MAP_COLS)

x = 1
y = MAP_COLS - 2
draw_map(map, screen)
character = pygame.image.load("Character\\normal_pose.png")
character = pygame.transform.scale(character, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
jumping = False
counter = 0
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if isWalkable(map, x, y - JUMP) and not jumping:
            jumping = True
            counter = JUMP
    if isWalkable(map, x + 1, y):
        x += SPEED
    if isWalkable(map, x, y + 1) and not jumping:
        y += GRAVITY
        updatePlace(screen, map, y - GRAVITY, x - SPEED)

    if jumping and counter != 0:
        y -= 1
        counter -= 1
        updatePlace(screen, map, y + 1, x - SPEED)
    if counter == 0:
        jumping = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    updatePlace(screen, map, y, x - 1)
    screen.blit(character, (x * SCALE, y * SCALE))
    pygame.display.update()
pygame.quit()
