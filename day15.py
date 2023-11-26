import common as c


def part_one(data, y):
    sensors = parse_input(data)

    # Calculate the Manhattan distance between every sensor-beacon pair
    distances = {s: c.manhattan(s, b) for s, b in sensors.items()}

    # Find out what sensor areas cover the row y
    ranges = covered_ranges(sensors, distances, y)
    ranges = merge_ranges(ranges)
    covered_positions = covered_positions_from_ranges(ranges)

    # Remove sensor positions that are right in the line
    sensors_over_line = len({sx for sx, sy in sensors if sy == y})

    # Remove beacon positions that are right in the line
    beacons_over_line = len({bx for bx, by in sensors.values() if by == y})

    return covered_positions - sensors_over_line - beacons_over_line


def part_two(data, max_y):
    sensors = parse_input(data)

    # Calculate the Manhattan distance between every sensor-beacon pair
    distances = {s: c.manhattan(s, b) for s, b in sensors.items()}

    for y in range(max_y + 1):
        # Find out what sensor areas cover the row y
        ranges = covered_ranges(sensors, distances, y)
        ranges = merge_ranges(ranges)
        if len(ranges) > 1:
            return (ranges[0][1] + 1) * 4_000_000 + y


def covered_ranges(sensors, distances, y):
    covered_ranges_x = list()
    for sx, sy in sensors:
        # Check if this sensor area covers the y row
        distance_s_to_y = abs(sy - y)
        distance_s_max = distances[(sx, sy)]
        if distance_s_to_y <= distance_s_max:
            # Calculate all x positions that fall in the y row
            diff = distance_s_max - distance_s_to_y
            covered_ranges_x.append((sx - diff, sx + diff))
    return covered_ranges_x


def merge_ranges(ranges: list[tuple]) -> list[tuple]:
    ranges.sort()
    merged_ranges = [ranges[0]]
    for cur_start, cur_end in ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        if cur_start <= last_end + 1:
            merged_ranges[-1] = (last_start, max(last_end, cur_end))
        else:
            merged_ranges.append((cur_start, cur_end))
    return merged_ranges


def covered_positions_from_ranges(ranges: list[tuple]):
    covered_positions = 0
    for rs, re in ranges:
        covered_positions += re - rs + 1
    return covered_positions


def parse_input(data) -> dict[tuple, tuple]:
    sensors = {}
    for line in c.strings(data):
        sx, sy, bx, by = c.ints(line)
        sensors[(sx, sy)] = (bx, by)
    return sensors


print(part_one(c.day(15), 2000000))
print(part_two(c.day(15), 4000000))
