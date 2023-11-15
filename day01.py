import common as c

raw_calories = c.strings(c.day(1))


def get_elf_calories(raw_calories):
    cur_calories = 0
    for calories in raw_calories:
        if not calories:
            yield cur_calories
            cur_calories = 0
            continue

        cur_calories += int(calories)
    yield cur_calories


elf_calories = sorted(get_elf_calories(raw_calories))

# part one: elf carrying the most calories

print(elf_calories[-1])

# part two: calories carried by the top 3 elves carrying the most calories

print(sum(elf_calories[-3:]))
