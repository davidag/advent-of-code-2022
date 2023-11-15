from functools import reduce
import common as c
import string


# part 1: sum of priorities of items in both compartments


def priority(c):
    if c in string.ascii_lowercase:
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27


def find_duplicated(rs):
    c1, c2 = rs[: len(rs) // 2], rs[len(rs) // 2 :]
    return (set(c1) & set(c2)).pop()


rucksacks = c.strings(c.day(3))

priorities = 0
for rs in rucksacks:
    priorities += priority(find_duplicated(rs))

print(priorities)

# part 2: sum of priorities of badges of each three-elf group


def find_common(rucksacks):
    rucksack_items = map(set, rucksacks)
    common_item = reduce(lambda x, y: x & y, rucksack_items)
    return common_item.pop()


priorities = 0
for group_rucksacks in c.chunked(rucksacks, 3):
    priorities += priority(find_common(group_rucksacks))

print(priorities)
