from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable

import common as c


# part 1: crates on top of each stack


class InputParser:
    def __init__(self, input):
        self.lines = c.strings(input)
        self.split_index = self.lines.index("")

    def initial_state(self) -> list[Stack]:
        state_lines = list(reversed(self.lines[: self.split_index]))
        stacks = list(map(Stack, state_lines[0].split()))

        for line in state_lines[1:]:
            for stack_id, idx in enumerate(range(1, len(line), 4)):
                crate = line[idx]
                if crate != " ":
                    stacks[stack_id].add(crate)

        return stacks

    def operations(self) -> Iterable[tuple]:
        for values in map(c.ints, self.lines[self.split_index + 1 :]):
            yield values


@dataclass
class Stack:
    id: str
    crates: list[str] = field(default_factory=list)

    def add(self, crate: str):
        self.crates.append(crate)

    def add_bulk(self, new_crates: list[str]):
        self.crates.extend(new_crates)

    def remove(self) -> str:
        return self.crates.pop()

    def remove_bulk(self, num) -> list[str]:
        removed_crates = self.crates[-num:]
        self.crates = self.crates[:-num]
        return removed_crates

    def top(self) -> str:
        return self.crates[-1]

    def __str__(self) -> str:
        return f"{self.id}: {self.crates}"


@dataclass
class CrateMover9000:
    stacks: list[Stack]

    def move(self, quantity, from_stack, to_stack):
        for _ in range(quantity):
            crate = stacks[from_stack - 1].remove()
            stacks[to_stack - 1].add(crate)

    def top_crates(self) -> str:
        return "".join([stack.top() for stack in self.stacks])


parser = InputParser(c.day(5))

stacks = parser.initial_state()
operator = CrateMover9000(stacks)

# apply each operation to the stacks
for move_params in parser.operations():
    operator.move(*move_params)

print(operator.top_crates())

# part 2: crates on top of each stack using a different crate mover


@dataclass
class CrateMover9001:
    stacks: list[Stack]

    def move(self, quantity, from_stack, to_stack):
        removed_crates = stacks[from_stack - 1].remove_bulk(quantity)
        stacks[to_stack - 1].add_bulk(removed_crates)

    def top_crates(self) -> str:
        return "".join([stack.top() for stack in self.stacks])


stacks = parser.initial_state()
operator = CrateMover9001(stacks)

# apply each operation to the stacks
for move_params in parser.operations():
    operator.move(*move_params)

print(operator.top_crates())
