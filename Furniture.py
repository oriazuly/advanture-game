from CollideTile import CollideTile
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


def create_desk(tiles, height, width, body_color, row, col):
    for floor in range(height):
        tiles[row][col - floor] = CollideTile(ALL_COLORS[body_color], row, col - floor)
        tiles[row + width][col - floor] = CollideTile(ALL_COLORS[body_color], row + width, col - floor)

    for block in range(width + 1):
        tiles[row + block][col - height] = CollideTile(ALL_COLORS[body_color], row + block, col - height)










#  def create_desk(tiles, height, width, body_color, row, col):
#     for floor in range(height):
#         tiles[row][col - floor] = CollideTile(ALL_COLORS[body_color], tiles[row][col - floor].getX(), tiles[row][col - floor].getY())
#         tiles[row + width][col - floor] = CollideTile(ALL_COLORS[body_color], tiles[row + width][col - floor].getX(), tiles[row + width][col - floor].getY())
#
#     for block in range(width + 1):
#         tiles[row + block][col - height] = CollideTile(ALL_COLORS["BL"], tiles[row + block][col - height].getX(), thatiles[row + block][col - height].getY())




