import common as c


# Part 1: get the sum of the signal strengths @ 20, 60, 100,... cycles

ops = c.strings(c.day(10))

strengths = []
next_strength = 20


def cpu(ops):
    reg_x = 1
    cycle = 1
    for op in ops:
        match op.split():
            case ["noop"]:
                yield cycle, reg_x
                cycle += 1
            case ["addx", v]:
                yield cycle, reg_x
                cycle += 1
                yield cycle, reg_x
                cycle += 1
                reg_x += int(v)


strengths = [
    cycle * reg_x for cycle, reg_x in cpu(ops) if cycle == 20 or (cycle - 20) % 40 == 0
]

print(sum(strengths))

# Part 2: print the crt using the value of reg x as the sprite postion

col = 0
for cycle, reg_x in cpu(ops):
    if reg_x - 1 <= col <= reg_x + 1:
        print("#", end="")
    else:
        print(".", end="")

    if col < 39:
        col += 1
    else:
        col = 0
        print("")
