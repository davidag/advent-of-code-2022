from dataclasses import dataclass

import common as c


@dataclass
class Range:
    ini: int
    end: int

    @staticmethod
    def from_str(value: str):
        return Range(*map(int, value.split("-")))

    def __str__(self) -> str:
        return f"{self.ini}-{self.end}"

    def __contains__(self, other) -> bool:
        return other.ini >= self.ini and other.end <= self.end

    def overlaps(self, other) -> bool:
        return self.ini <= other.end and self.end >= other.ini


# input parsing
def make_range_pair(line: str) -> tuple[Range, Range]:
    return tuple(Range.from_str(r) for r in line.split(","))


pairs = map(make_range_pair, c.strings(c.day(4)))

# parts 1 and 2
num_fully_contained = 0
num_overlapping = 0

for r1, r2 in pairs:
    if r1 in r2 or r2 in r1:
        num_fully_contained += 1

    if r1.overlaps(r2):
        num_overlapping += 1


print(num_fully_contained)
print(num_overlapping)
