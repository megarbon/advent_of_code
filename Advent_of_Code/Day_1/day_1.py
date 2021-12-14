from itertools import tee

def pairwise(it):
    """Mock `itertools.pairwise` for Python versions below 3.10."""
    prev_, next_ = tee(it, 2)     # Split `it` into two iterables.
    next(next_)                   # Advance once.
    yield from zip(prev_, next_)  # Yield the pairs.

with open(input, "r") as f:
    depths = (int(line) for line in f)

    count = 0
    for prev_, next_ in pairwise(depths):
        if prev_ < next_:
            count += 1

    print(count)