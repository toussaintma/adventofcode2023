#!/usr/bin/python3

filename = "input.txt"
fin = open(filename)
lines = fin.readlines()
print(f"Reading file {filename}")

grid = []
for line in lines:
    grid.append([*line.strip().replace("\\", "L")])
width = len(grid[0])
height = len(grid)

for l in grid:
    print(l)
print(f"We have a grid of width {width} and height {height}")

beams = [[0, 0, "e"]]  # [x, y, dir]
visited = []


def get_next_pos(pos):
    result = []
    if pos[2] == "e":
        result = [pos[0] + 1, pos[1], pos[2]]
    if pos[2] == "n":
        result = [pos[0], pos[1] - 1, pos[2]]
    if pos[2] == "w":
        result = [pos[0] - 1, pos[1], pos[2]]
    if pos[2] == "s":
        result = [pos[0], pos[1] + 1, pos[2]]
    if result[0] < 0 or result[0] >= width or result[1] < 0 or result[1] >= height:
        result = []
    return result


def is_straight(tile):
    move = grid[tile[1]][tile[0]]
    result = False
    if move == ".":
        result = True
    if move == "-" and (tile[2] in "ew"):
        result = True
    if move == "|" and (tile[2] in "ns"):
        result = True
    return result


def get_beams(tile):
    b = []
    move = grid[tile[1]][tile[0]]
    print(f"At [{tile[0]}, {tile[1]}] going {tile[2]} we have a crossroad {move}")
    if move == "/":
        if tile[2] == "e":
            b.append(get_next_pos([tile[0], tile[1], "n"]))
        if tile[2] == "n":
            b.append(get_next_pos([tile[0], tile[1], "e"]))
        if tile[2] == "w":
            b.append(get_next_pos([tile[0], tile[1], "s"]))
        if tile[2] == "s":
            b.append(get_next_pos([tile[0], tile[1], "w"]))
    if move == "L":
        if tile[2] == "e":
            b.append(get_next_pos([tile[0], tile[1], "s"]))
        if tile[2] == "n":
            b.append(get_next_pos([tile[0], tile[1], "w"]))
        if tile[2] == "w":
            b.append(get_next_pos([tile[0], tile[1], "n"]))
        if tile[2] == "s":
            b.append(get_next_pos([tile[0], tile[1], "e"]))
    if move == "|":
        b.append(get_next_pos([tile[0], tile[1], "n"]))
        b.append(get_next_pos([tile[0], tile[1], "s"]))
    if move == "-":
        b.append(get_next_pos([tile[0], tile[1], "e"]))
        b.append(get_next_pos([tile[0], tile[1], "w"]))
    result = list(filter(lambda x: len(x) > 0, b))
    print(f"  Proposing new beams: {result}")
    return result


while len(beams) > 0:
    b = beams.pop()
    next_pos = b
    while len(next_pos) > 0:
        visited.append(next_pos)
        print(f"Visited {next_pos}")
        if not is_straight(next_pos):
            for i in get_beams(next_pos):
                if not i in visited:
                    beams.append(i)
                    print(f"Adding new beam: {i}")
            next_pos = []
        else:
            next_pos = get_next_pos(next_pos)
print(f"No more beams to follow")
print(f"Visited nodes: {visited}")
energized = []
for i in visited:
    if not [i[0], i[1]] in energized:
        energized.append([i[0], i[1]])
print(f"energized nodes: {energized}")

print()
print(f"The number of energized cells is {len(energized)}")
fin.close()
