import common as c

# part 1: positions visited by tail with 2 nodes (head and tail)


def follow(p1, p2):
    x, y = p1[0], p1[1]
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]

    if dx > 1:
        x += 1
    elif dx < -1:
        x -= 1
    elif dy > 1:
        y += 1
    elif dy < -1:
        y -= 1

    if dx == 2 or dx == -2:
        y = y - 1 if dy < 0 else y + 1 if dy > 0 else y
    elif dy == 2 or dy == -2:
        x = x - 1 if dx < 0 else x + 1 if dx > 0 else x

    return (x, y)


moves = c.strings(c.day(9))

head = tail = (0, 0)
visited = {tail}
directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}

for m in moves:
    op, d = m.split()
    d = int(d)
    for _ in range(d):
        head = (head[0] + directions[op][0], head[1] + directions[op][1])
        tail = follow(tail, head)
        visited.add(tail)

print(len(visited))

# part 2: positions visited by tail when there are 10 knots

knots = [(0, 0) for _ in range(10)]
visited = {knots[0]}

for m in moves:
    op, d = m.split()
    d = int(d)
    for _ in range(d):
        knots[0] = (knots[0][0] + directions[op][0], knots[0][1] + directions[op][1])
        for k in range(1, len(knots)):
            knots[k] = follow(knots[k], knots[k - 1])
        # save the tail position
        visited.add(knots[len(knots) - 1])

print(len(visited))
