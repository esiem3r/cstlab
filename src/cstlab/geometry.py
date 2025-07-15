"""
geometry.py – spiral/shell utilities for Carry‑Symmetric Topology
-----------------------------------------------------------------

Doctest quick‑check:

>>> spiral_index((0, 0))
0
>>> spiral_index((1, 0))
1
>>> inverse_index(1)
(1, 0)
>>> sorted(shell_Linf(2))[:4]
[(-2, -2), (-2, -1), (-2, 0), (-2, 1)]
"""
from __future__ import annotations

from math import isqrt
from typing import Iterable, Tuple

Point = Tuple[int, int]


# ----------------------------------------------------------------------
# Spiral index (CW, start on (r, -r))
# ----------------------------------------------------------------------
def shell_size_Linf(r: int) -> int:
    """Number of lattice points on an L‑inf shell."""
    return 1 if r == 0 else 8 * r


def spiral_index(pt: Point) -> int:
    """Map lattice point → spiral index (square spiral, clockwise)."""
    x, y = pt
    r = max(abs(x), abs(y))
    if r == 0:
        return 0
    offset = 1 + 4 * (r - 1) * r  # N(r‑1)
    # locate position along perimeter
    if y == -r:
        pos = x + r
    elif x == -r:
        pos = 2 * r + (y + r)
    elif y == r:
        pos = 4 * r + (-x + r)
    else:  # x == r
        pos = 6 * r + (-y + r)
    return offset + pos


def inverse_index(n: int) -> Point:
    """Inverse map: spiral index → lattice point."""
    if n == 0:
        return (0, 0)
    # find minimal r with N(r) ≥ n
    r = isqrt(n // 4) + 2
    while 1 + 4 * r * (r + 1) < n:
        r += 1
    while n <= 1 + 4 * (r - 1) * r:
        r -= 1
    offset = 1 + 4 * (r - 1) * r
    pos = n - offset
    if pos < 2 * r:
        return (pos - r, -r)
    pos -= 2 * r
    if pos < 2 * r:
        return (-r, pos - r)
    pos -= 2 * r
    if pos < 2 * r:
        return (r - pos, r)
    pos -= 2 * r
    return (r, r - pos)


# ----------------------------------------------------------------------
# Shell generators
# ----------------------------------------------------------------------
def shell_Linf(r: int) -> Iterable[Point]:
    """Yield points on the Chebyshev (square) shell of radius r."""
    if r == 0:
        yield (0, 0)
        return
    x = -r
    for y in range(-r, r):
        yield (x, y)              # left edge
    for x in range(-r, r):
        yield (x, r)              # top edge
    for y in range(r, -r, -1):
        yield (r, y)              # right edge
    for x in range(r, -r, -1):
        yield (x, -r)             # bottom edge


def shell_L1(r: int) -> Iterable[Point]:
    """Yield points on the Manhattan (diamond) shell of radius r."""
    if r == 0:
        yield (0, 0)
        return
    for x in range(-r, r + 1):
        y = r - abs(x)
        yield (x, y)
        if y:
            yield (x, -y)


__all__ = [
    "Point",
    "spiral_index",
    "inverse_index",
    "shell_Linf",
    "shell_L1",
    "shell_size_Linf",
]
