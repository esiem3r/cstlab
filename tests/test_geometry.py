import random
from cstlab.geometry import (
    spiral_index,
    inverse_index,
    shell_Linf,
    shell_size_Linf,
)

def test_roundtrip_small():
    pts = [(x, y) for x in range(-3, 4) for y in range(-3, 4)]
    for p in pts:
        assert inverse_index(spiral_index(p)) == p

def test_monotone_shell():
    # indices strictly increase as radius grows
    last = 0
    for r in range(1, 15):
        for p in shell_Linf(r):
            idx = spiral_index(p)
            assert idx > last
            last = idx

def test_random_inverse():
    for _ in range(1_000):
        r = random.randint(0, 30)
        size = shell_size_Linf(r)
        n = random.randint(0, size - 1) + (1 + 4 * (r - 1) * r if r else 0)
        assert spiral_index(inverse_index(n)) == n
