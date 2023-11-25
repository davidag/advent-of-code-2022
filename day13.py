import ast
from functools import cmp_to_key
from itertools import chain, zip_longest
import common as c


def part_one(data):
    packet_pairs = parse_input(data)
    packets_in_right_order = []
    for i, pair in enumerate(packet_pairs, 1):
        if right_order(*pair) < 0:
            packets_in_right_order.append(i)
    return sum(packets_in_right_order)


def part_two(data):
    packets = chain(*parse_input(data), [[[2]], [[6]]])
    packets = sorted(packets, key=cmp_to_key(right_order))
    divider1_idx = packets.index([[2]]) + 1
    divider2_idx = packets.index([[6]]) + 1
    return divider1_idx * divider2_idx


def right_order(packet1, packet2):
    for v1, v2 in zip_longest(packet1, packet2):
        match v1, v2:
            case _, None:
                return 1
            case None, _:
                return -1
            case int(), int():
                if v1 < v2:
                    return -1
                if v1 > v2:
                    return 1
            case _:
                v1 = v1 if isinstance(v1, list) else [v1]
                v2 = v2 if isinstance(v2, list) else [v2]
                if (res := right_order(v1, v2)) != 0:
                    return res
    return 0


def parse_input(data):
    lines = c.strings(data)
    i = 0
    while i < len(lines):
        packet1 = ast.literal_eval(lines[i])
        packet2 = ast.literal_eval(lines[i + 1])
        yield packet1, packet2
        i += 3


print(part_one(c.day(13)))
print(part_two(c.day(13)))
