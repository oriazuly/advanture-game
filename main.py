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
y = 1
character = pygame.image.load("Character\\normal_pose.png")
character = pygame.transform.scale(character, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= SPEED
        if not isWalkable(map, x, y):
            y += SPEED
    if keys[pygame.K_s]:
        y += SPEED
        if not isWalkable(map, x, y):
            y -= SPEED
    if keys[pygame.K_d]:
        x += SPEED
        if not isWalkable(map, x, y):
            x -= SPEED
        if character != "Character\\normal_pose.png":
            character = pygame.image.load("Character\\normal_pose.png")
            character = pygame.transform.scale(character, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    if keys[pygame.K_a]:
        x -= SPEED
        if not isWalkable(map, x, y):
            x += SPEED

        if character != "Character\\reverse_pose.png":
            character = pygame.image.load("Character\\reverse_pose.png")
            character = pygame.transform.scale(character, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_map(map, screen)
    screen.blit(character, (x * SCALE, y * SCALE))
    pygame.display.update()
pygame.quit()
