from itertools import takewhile
import common as c


# part 1: visible trees from outside the grid

map = c.matrix(c.day(8))
nrows = len(map)
ncols = len(map[0])

visible = set()

for i in range(nrows):
    # left to right
    visible.add((i, 0))
    highest_seen = 0
    for j in range(1, ncols):
        highest_seen = max(highest_seen, map[i][j - 1])
        if map[i][j] > highest_seen:
            visible.add((i, j))

    # right to left
    visible.add((i, ncols - 1))
    highest_seen = 0
    for j in range(ncols - 2, 0, -1):
        highest_seen = max(highest_seen, map[i][j + 1])
        if map[i][j] > highest_seen:
            visible.add((i, j))

for j in range(ncols):
    # top to bottom
    visible.add((0, j))
    highest_seen = 0
    for i in range(1, nrows):
        highest_seen = max(highest_seen, map[i - 1][j])
        if map[i][j] > highest_seen:
            visible.add((i, j))

    # bottom to top
    visible.add((nrows - 1, j))
    highest_seen = 0
    for i in range(nrows - 2, 0, -1):
        highest_seen = max(highest_seen, map[i + 1][j])
        if map[i][j] > highest_seen:
            visible.add((i, j))

print(len(visible))

# part 2: max scenic score (product of viewing distances)

max_scenic_score = 0

for i in range(nrows):
    for j in range(ncols):
        this = map[i][j]

        dleft = len(list(takewhile(lambda x: x < this, reversed(map[i][0:j]))))
        if j - dleft >= 1:
            dleft += 1

        dright = len(list(takewhile(lambda x: x < this, map[i][j + 1 :])))
        if j + dright < ncols - 1:
            dright += 1

        dtop = takewhile(lambda x: x < this, [map[t][j] for t in range(i - 1, 0, -1)])
        dtop = len(list(dtop))
        if i - dtop >= 1:
            dtop += 1

        dbottom = takewhile(
            lambda x: x < this, [map[t][j] for t in range(i + 1, nrows)]
        )
        dbottom = len(list(dbottom))
        if i + dbottom < nrows - 1:
            dbottom += 1

        max_scenic_score = max(max_scenic_score, dleft * dright * dtop * dbottom)


print(max_scenic_score)
