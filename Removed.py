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


