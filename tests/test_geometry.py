import random

from cstlab.geometry import (
    inverse_index,
    shell_Linf,
    shell_size_Linf,
    spiral_index,
)


def test_roundtrip_small():
    pts = [(x, y) for x in range(-3, 4) for y in range(-3, 4)]
    for p in pts:
        assert inverse_index(spiral_index(p)) == p


def test_monotone_shell():
    last = 0
    for r in range(1, 15):
        for p in shell_Linf(r):
            idx = spiral_index(p)
            assert idx > last
            last = idx


def test_random_inverse():
    rng = random.Random(0xC57)
    for _ in range(1_000):
        r = rng.randint(0, 30)
        base = 0 if r == 0 else 1 + 4 * (r - 1) * r
        n = base + rng.randrange(shell_size_Linf(r))
        assert spiral_index(inverse_index(n)) == n
