from Constants import *
import Functions


class Camera:
    x = 0
    y = 0

    def update():
        pass

    def __draw_map(screen, tiles):
        Functions.draw_map(tiles, screen, (Camera.x, Camera.y))

    def __draw_player(screen, character):
        screen.blit(character.getImageSrc(), (character.getX() * SCALE - Camera.x, character.getY() * SCALE - Camera.y))

    def draw(screen, tiles, character, space, text):
        Camera.x = character.getX() * SCALE - SCREEN_WIDTH / 2  # Camera.x is already scaled so you don`t need to scale it later on
        Camera.__draw_map(screen, tiles)
        Camera.__view_text(screen, space, text)
        Camera.__draw_player(screen, character)

    def reset():
        x = 0
        y = 0

    def __view_text(screen, space, text):
        font_name = "Ariel"
        text_size = 50
        color = (0, 255, 120)
        x_pos = X_TEXT_POS - space
        y_pos = Y_TEXT_POS
        font = pygame.font.SysFont(font_name, text_size)
        screen.blit(font.render(text, True, color), (x_pos, y_pos))