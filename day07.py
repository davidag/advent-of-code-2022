from __future__ import annotations
from dataclasses import dataclass, field

import common as c


@dataclass
class Directory:
    name: str
    parent: Directory | None = None
    files: dict[str, int] = field(default_factory=dict)
    subdirs: dict[str, Directory] = field(default_factory=dict)

    @property
    def path(self):
        if self.parent is None:
            return self.name
        parent = self.parent.path
        if parent == "/":
            return f"/{self.name}"
        else:
            return f"{parent}/{self.name}"


class FileSystem:
    def __init__(self, root: Directory):
        self.root = root

    def get_directory_sizes(self, result: dict, dir=None) -> int:
        if dir is None:
            dir = self.root

        dir_size = sum(dir.files.values())
        for subdir in dir.subdirs.values():
            dir_size += self.get_directory_sizes(result, subdir)

        result[dir.path] = dir_size
        return dir_size


class FileSystemBuilder:
    def _ls(self, contents):
        for name, type_or_size in contents.items():
            if type_or_size == "dir":
                self.curr.subdirs[name] = Directory(name, self.curr)
            else:
                self.curr.files[name] = int(type_or_size)

    def _cd(self, dir):
        if dir == "..":
            self.curr = self.curr.parent
        else:
            self.curr = self.curr.subdirs[dir]

    def from_commands(self, commands: list[str]) -> FileSystem:
        self.root = Directory("/")
        self.curr = self.root
        i = 1
        while i < len(commands):
            match commands[i].split():
                case ["$", "cd", dir]:
                    self._cd(dir)
                case ["$", "ls"]:
                    contents = {}
                    while i + 1 < len(commands) and not commands[i + 1].startswith("$"):
                        type_or_size, name = commands[i + 1].split()
                        contents[name] = type_or_size
                        i += 1
                    self._ls(contents)
                case _:
                    raise ValueError(f"Unexpected command: {commands[i]}")
            i += 1

        return FileSystem(self.root)


commands = c.strings(c.day(7))

builder = FileSystemBuilder()
filesystem = builder.from_commands(commands)

dir_sizes = {}
filesystem.get_directory_sizes(dir_sizes)

print(sum(s for s in dir_sizes.values() if s < 100000))

total_space = 70_000_000
free_space = total_space - dir_sizes["/"]
required_space = 30_000_000 - free_space

print(min(s for s in dir_sizes.values() if s >= required_space))
