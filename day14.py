from itertools import count
import common as c


def part_one(data):
    grid = parse_input(data)
    floor_y = 500
    for unit in count():
        _, sand_y = simulate_sand(grid, floor_y)
        if sand_y == floor_y - 1:
            return unit


def part_two(data):
    grid = parse_input(data)
    floor_y = max(y for _, y in grid) + 2
    for unit in count():
        sand_coords = simulate_sand(grid, floor_y)
        if sand_coords == (500, 0):
            return unit + 1


def simulate_sand(grid, floor_y):
    x, y = 500, 0
    while True:
        if y + 1 == floor_y:
            grid[(x, y)] = "o"
            return x, y

        if (x, y + 1) not in grid:
            y += 1
        elif (x - 1, y + 1) not in grid:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in grid:
            x, y = x + 1, y + 1
        else:
            grid[(x, y)] = "o"
            return x, y


def parse_input(data):
    grid = {}
    for line in c.strings(data):
        points = line.split("->")
        for p in range(0, len(points) - 1):
            p0_x, p0_y = map(int, points[p].split(","))
            p1_x, p1_y = map(int, points[p + 1].split(","))
            if p0_x == p1_x:
                for y in range(min(p0_y, p1_y), max(p0_y, p1_y) + 1):
                    grid[(p0_x, y)] = "#"
            else:
                for x in range(min(p0_x, p1_x), max(p0_x, p1_x) + 1):
                    grid[(x, p0_y)] = "#"
    return grid


print(part_one(c.day(14)))
print(part_two(c.day(14)))
