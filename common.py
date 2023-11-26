from functools import partial
from itertools import islice
import re


def day(n):
    '''Load the input for day "n"'''
    return open("inputs/input{n:02d}".format(n=n)).read()


def example(n, x):
    return open("inputs/example{n:02d}{x}".format(n=n, x=x)).read()


def ints(data):
    """Return a tuple of ints from a string"""
    return tuple(int(x) for x in re.findall(r"[-+]?\d+", data))


def strings(data):
    """Return a list of strings from a string of multiple lines"""
    return data.splitlines()


def vector(data, sep=","):
    """Return a int list from comma-separated string of integers"""
    return [int(x) for x in data.split(sep)]


def matrix(data):
    """Return a list of list of ints from a string matrix with one row per line."""
    return [[int(x) for x in row] for row in data.splitlines()]


def col(data, c):
    return [d[c] for d in data]


def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(islice(iterable, n))


def chunked(iterable, n):
    """Break iterable into lists of size n"""
    return iter(partial(take, n, iter(iterable)), [])


def print_grid(g):
    min_x, max_x = min(x for x, _ in g), max(x for x, _ in g)
    min_y, max_y = min(y for _, y in g), max(y for _, y in g)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            v = g.get((x, y))
            if v is None:
                print(".", end="")
            else:
                print(v, end="")
        print("")
