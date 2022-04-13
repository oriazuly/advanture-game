def generate_map(rows, cols):  # auto create normal unchangeable map
    map = []
    for row in range(rows):
        new_line = []
        for col in range(cols):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                new_line.append("X")
            else:
                random_value = random.randint(1, 100)
                if random_value < 95:
                    new_line.append("CABB")
                elif 95 < random_value < 97:
                    new_line.append("COLE")
                elif 97 < random_value < 99:
                    new_line.append("IRON")
                else:
                    new_line.append("MOISTY")

        map.append(new_line)
    return map


def print_map(map):  # print the map
    for row in range(len(map)):
        for col in range(len(map[row])):
            print(map[row][col], end=", ")
        print()


def print_tiles(tiles):
    for row in range(len(tiles)):
        for col in range(len(tiles[row])):
            if tiles[row][col].getType() == "C":
                print("c", end="")
            else:
                print("b", end="")
        print()


def updatePlace(screen, map, col, row):  # if the map not moving
    tile = Constants.ALL_COLORS[map[row][col]]
    pygame.transform.scale(tile, (20, 20))
    screen.blit(tile, (row * Constants.SCALE, col * Constants.SCALE))






def create_chandeliers(amount, space, tiles, body_color, light_color, row, col):
    for chandelier in range(amount):
        location = row + chandelier * space
        if 3 < location < MAP_ROWS - 3:
            create_chandelier(tiles, body_color, light_color, location, col)


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

    tiles[row][col + 5].setImgSrc(BASIC_COLORS[light_color])
    tiles[row + 2][col + 5].setImgSrc(BASIC_COLORS[light_color])
    tiles[row - 2][col + 5].setImgSrc(BASIC_COLORS[light_color])


def create_low_chandelier(tiles, body_color, light_color, row, col):
    tiles[row][col].setImgSrc(BASIC_COLORS[body_color])

    tiles[row][col + 1].setImgSrc(BASIC_COLORS[body_color])
    tiles[row + 1][col + 1].setImgSrc(BASIC_COLORS[body_color])
    tiles[row - 1][col + 1].setImgSrc(BASIC_COLORS[body_color])

    tiles[row][col + 2].setImgSrc(BASIC_COLORS[body_color])
    tiles[row + 1][col + 2].setImgSrc(BASIC_COLORS[light_color])
    tiles[row - 1][col + 2].setImgSrc(BASIC_COLORS[light_color])

    tiles[row][col + 3].setImgSrc(BASIC_COLORS[light_color])


def create_desk(tiles, height, width, body_color, row, col):
    for floor in range(height):
        tiles[row][col - floor] = CollideTile(ALL_COLORS[body_color], tiles[row][col - floor].getX(), tiles[row][col - floor].getY())
        tiles[row + width][col - floor] = CollideTile(ALL_COLORS[body_color], tiles[row + width][col - floor].getX(), tiles[row + width][col - floor].getY())

    for block in range(width + 1):
        tiles[row + block][col - height] = CollideTile(ALL_COLORS[body_color], tiles[row + block][col - height].getX(), tiles[row + block][col - height].getY())


def create_border(tiles, height, width, body_color, row, col):
    for i in range(height):
        for j in range(width):
            tiles[row + i][col - j] = CollideTile(COLLIDER_COLORS[body_color], tiles[row + i][col - j].getX(), tiles[row + i][col - j].getY())
