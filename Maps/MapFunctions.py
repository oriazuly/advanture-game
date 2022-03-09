import MapConstants


def generate_map(rows, cols):
    map = []
    for row in range(rows):
        new_line = []
        for col in range(cols):
            new_line.append("Y")
        map.append(new_line)
    return map


def write_map(map_name, rows, cols):
    f = open(map_name, "w")
    for row in range(rows):
        for col in range(cols):
            f.write("Y ")
        f.write("\n")

def read_map():
    pass


def print_map(map):
    for row in range(len(map)):
        for col in range(len(map[row])):
            print(map[row][col], end=", ")
        print()


def draw_map(map, screen):
    for row in range(len(map)):
        for col in range(len(map[row])):
            tile = Constants.COLORS[map[row][col]]
            screen.blit(tile, (row * Constants.SCALE, col * Constants.SCALE))