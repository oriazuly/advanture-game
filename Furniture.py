from Constants import *


def create_chandelier(tiles, body_color, light_color, row, col):
    tiles[row][col].setImgSrc(BASIC_COLORS[body_color])
    tiles[row][col + 1].setImgSrc(BASIC_COLORS[body_color])
    tiles[row][col + 2].setImgSrc(BASIC_COLORS[body_color])

    tiles[row][col + 3].setImgSrc(BASIC_COLORS[body_color])
    tiles[row + 1][col + 3].setImgSrc(BASIC_COLORS[body_color])
    tiles[row - 1][col + 3].setImgSrc(BASIC_COLORS[body_color])
    tiles[row + 2][col + 3].setImgSrc(BASIC_COLORS[body_color])
    tiles[row - 2][col + 3].setImgSrc(BASIC_COLORS[body_color])

    tiles[row][col + 4].setImgSrc(BASIC_COLORS[body_color])
    tiles[row + 2][col + 4].setImgSrc(BASIC_COLORS[body_color])
    tiles[row - 2][col + 4].setImgSrc(BASIC_COLORS[body_color])

    tiles[row][col + 5].setImgSrc(BASIC_COLORS[body_color])
    tiles[row + 2][col + 5].setImgSrc(BASIC_COLORS[light_color])
    tiles[row - 2][col + 5].setImgSrc(BASIC_COLORS[light_color])

    tiles[row][col + 5].setImgSrc(BASIC_COLORS[light_color])

def create_desk(tiles, body_color, row, col):
    tiles[row][col].setImgSrc(ALL_COLORS[body_color])



