import heapq
import common as c


def part_one(data):
    return a_star(*parse_input(data))


def part_two(data):
    map, _, end = parse_input(data)
    return min(a_star(map, start, end) for start in map if map[start] == 0)


def a_star(map, start, end):
    costs = {start: 0}
    frontier = [(0, start)]

    while frontier:
        _, position = heapq.heappop(frontier)
        if position == end:
            return costs[end]
        for candidate in candidate_positions(map, position):
            candidate_cost = costs[position] + 1
            if candidate not in costs or candidate_cost < costs[candidate]:
                costs[candidate] = candidate_cost
                heapq.heappush(
                    frontier, (candidate_cost + manhattan(candidate, end), candidate)
                )

    return float("inf")


def candidate_positions(map, pos):
    moves = {(0, 1), (1, 0), (-1, 0), (0, -1)}
    for di, dj in moves:
        candidate = (pos[0] + di, pos[1] + dj)
        if candidate in map and map[candidate] <= map[pos] + 1:
            yield candidate


def manhattan(pos_a, pos_b) -> int:
    (x1, y1), (x2, y2) = pos_a, pos_b
    return abs(x1 - x2) + abs(y1 - y2)


def parse_input(data):
    map = {}
    start, end = None, None
    for i, row in enumerate(c.strings(data)):
        for j, height in enumerate(row):
            match height:
                case "S":
                    start = (i, j)
                    map[(i, j)] = ord("a") - ord("a")
                case "E":
                    end = (i, j)
                    map[(i, j)] = ord("z") - ord("a")
                case _:
                    map[(i, j)] = ord(height) - ord("a")
    return map, start, end


print(part_one(c.day(12)))
print(part_two(c.day(12)))
