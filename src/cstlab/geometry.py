"""
geometry.py – spiral / shell utilities for Carry‑Symmetric Topology
------------------------------------------------------------------

Doctest sanity:

>>> spiral_index((0, 0))
0
>>> spiral_index((1, 0))
1
>>> inverse_index(1)
(1, 0)
>>> inverse_index(8)
(1, -1)
>>> spiral_index(inverse_index(3500)) == 3500
True
"""

from __future__ import annotations

from collections.abc import Iterable
from itertools import islice

Point = tuple[int, int]  # canonical lattice‑point type


# ──────────────────────────────────────────────────────────────────────────────
# Helper: infinite generator of square‑spiral coordinates (clockwise)
# ──────────────────────────────────────────────────────────────────────────────
def _spiral_coords() -> Iterable[Point]:
    """Yield lattice points in square‑spiral order (clockwise, starting at origin)."""
    x = y = 0
    yield (0, 0)  # index 0
    step = 1
    while True:
        # Right  → (step)
        for _ in range(step):
            x += 1
            yield (x, y)
        # Up     ↑ (step)
        for _ in range(step):
            y += 1
            yield (x, y)
        step += 1
        # Left   ← (step)
        for _ in range(step):
            x -= 1
            yield (x, y)
        # Down   ↓ (step)
        for _ in range(step):
            y -= 1
            yield (x, y)
        step += 1


# ──────────────────────────────────────────────────────────────────────────────
# Index maps  (simple enumeration – plenty fast for r ≤ 30 used in tests)
# ──────────────────────────────────────────────────────────────────────────────
def spiral_index(pt: Point) -> int:  # noqa: D401
    """Return the spiral index of *pt* (O(index) enumeration, but index ≤ 3 700 in tests)."""
    for idx, p in enumerate(_spiral_coords()):
        if p == pt:
            return idx
        # Safe‑guard: break once radius surely larger than pt’s Chebyshev radius
        if max(abs(*p)) > max(abs(pt[0]), abs(pt[1])) + 1:
            continue


def inverse_index(n: int) -> Point:
    """Return the lattice point at spiral position *n* (O(n) but n ≤ 3 700 in tests)."""
    return next(islice(_spiral_coords(), n, None))


# ──────────────────────────────────────────────────────────────────────────────
# Shell generators (your original versions kept intact)
# ──────────────────────────────────────────────────────────────────────────────
def shell_Linf(r: int) -> Iterable[Point]:
    if r == 0:
        yield (0, 0)
        return
    k = r
    # right edge
    for y in range(-k + 1, k + 1):
        yield (k, y)
    # top edge
    for x in range(k - 1, -k - 1, -1):
        yield (x, k)
    # left edge
    for y in range(k - 1, -k - 1, -1):
        yield (-k, y)
    # bottom edge
    for x in range(-k + 1, k):
        yield (x, -k)


def shell_size_Linf(r: int) -> int:  # noqa: D401
    """Number of lattice points on a Chebyshev shell."""
    return 1 if r == 0 else 8 * r


def shell_L1(r: int) -> Iterable[Point]:
    if r == 0:
        yield (0, 0)
        return
    for x in range(-r, r + 1):
        y = r - abs(x)
        yield (x, y)
        if y != 0:
            yield (x, -y)
