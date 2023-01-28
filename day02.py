import common as c


rounds = [tuple(l.split(" ")) for l in c.strings(c.day(2))]


def score(r):
    shape = {"X": 1, "Y": 2, "Z": 3}
    outcome = {
            ("A", "X"): 3, ("A", "Y"): 6, ("A", "Z"): 0,
            ("B", "X"): 0, ("B", "Y"): 3, ("B", "Z"): 6,
            ("C", "X"): 6, ("C", "Y"): 0, ("C", "Z"): 3,
    }
    return shape[r[1]] + outcome[r]

# part 1

print(sum(score(r) for r in rounds))

# part 2

def decrypt_rounds(rounds):
    # the second column describes how the round is expected to end
    expected = {
            ("A", "X"): "Z", ("A", "Y"): "X", ("A", "Z"): "Y",
            ("B", "X"): "X", ("B", "Y"): "Y", ("B", "Z"): "Z",
            ("C", "X"): "Y", ("C", "Y"): "Z", ("C", "Z"): "X",
    }
    for r in rounds:
        yield (r[0], expected[r])


print(sum(score(r) for r in decrypt_rounds(rounds)))
