from __future__ import annotations
from dataclasses import dataclass
from typing import Callable
import math
import re

import common as c


# Part 1: calculate level of monkey business after 20 rounds


@dataclass
class Monkey:
    items: list[int]
    op: str
    test_num: int
    test_res: dict[bool, int]
    inspected_counter: int = 0

    def __post_init__(self):
        self._original_items = self.items.copy()

    def add(self, item):
        self.items.append(item)

    def run(self, all_monkeys: list[Monkey], manage_worry: Callable[[int], int]):
        for old in self.items:
            inter = eval(self.op)
            new = manage_worry(inter)
            dest_monkey = self.test_res[new % self.test_num == 0]
            all_monkeys[dest_monkey].add(new)
            self.inspected_counter += 1
        self.items.clear()

    def reset(self):
        self.items = self._original_items.copy()
        self.inspected_counter = 0


lines = c.strings(c.day(11))
monkeys = []

# initialize monkeys
for _, items, op, test, true, false, _ in c.chunked(lines, 7):
    items = [int(x) for x in items.split(":")[1].split(",")]
    op = op.split("=")[1].strip()
    test = int(re.findall(r"\d+", test)[0])
    true = int(re.findall(r"\d+", true)[0])
    false = int(re.findall(r"\d+", false)[0])
    monkeys.append(Monkey(items, op, test, {True: true, False: false}))

# run the game for 20 rounds
for _ in range(20):
    for monkey in monkeys:
        monkey.run(monkeys, lambda x: math.floor(x / 3))

# get two top monkey inspectors
monkey_inspections = sorted([m.inspected_counter for m in monkeys], reverse=True)

# print level of monkey business
print(monkey_inspections[0] * monkey_inspections[1])


# part 2: find the new monkey business after a long time!


for monkey in monkeys:
    monkey.reset()

# we avoid having numbers larger than the lcm of all divisible check values
lcm = math.lcm(*[m.test_num for m in monkeys])

for _ in range(10000):
    for idx, monkey in enumerate(monkeys):
        monkey.run(monkeys, lambda x: x % lcm)

# get two top monkey inspectors
monkey_inspections = sorted([m.inspected_counter for m in monkeys], reverse=True)

# print level of monkey business
print(monkey_inspections[0] * monkey_inspections[1])
