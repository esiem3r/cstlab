"""
geometry.py – spiral / shell utilities for Carry‑Symmetric Topology
------------------------------------------------------------------

Doctest sanity
--------------

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
# Infinite generator of square‑spiral coordinates (clockwise)
# ──────────────────────────────────────────────────────────────────────────────
def _spiral_coords() -> Iterable[Point]:
    x = y = 0
    yield (0, 0)  # index 0
    step = 1
    while True:
        # → right
        for _ in range(step):
            x += 1
            yield (x, y)
        # ↑ up
        for _ in range(step):
            y += 1
            yield (x, y)
        step += 1
        # ← left
        for _ in range(step):
            x -= 1
            yield (x, y)
        # ↓ down
        for _ in range(step):
            y -= 1
            yield (x, y)
        step += 1


# ──────────────────────────────────────────────────────────────────────────────
# Index maps  (enumerative – fine for r ≤ 30 in tests)
# ──────────────────────────────────────────────────────────────────────────────
def spiral_index(pt: Point) -> int:
    """Return the spiral index of *pt* (O(index) enumeration; fine for tests)."""
    target_r = max(abs(pt[0]), abs(pt[1]))
    for idx, p in enumerate(_spiral_coords()):
        if p == pt:
            return idx
        if max(abs(p[0]), abs(p[1])) > target_r + 1:
            continue
    raise RuntimeError("Point not found (logic error)")


def inverse_index(n: int) -> Point:
    """Return lattice point at spiral position *n* (enumerative, but n ≤ 3 700)."""
    return next(islice(_spiral_coords(), n, None))


# ──────────────────────────────────────────────────────────────────────────────
# Shell generators
# ──────────────────────────────────────────────────────────────────────────────
def shell_Linf(r: int) -> Iterable[Point]:
    if r == 0:
        yield (0, 0)
        return
    k = r
    for y in range(-k + 1, k + 1):  # right edge
        yield (k, y)
    for x in range(k - 1, -k - 1, -1):  # top edge
        yield (x, k)
    for y in range(k - 1, -k - 1, -1):  # left edge
        yield (-k, y)
    for x in range(-k + 1, k):  # bottom edge
        yield (x, -k)


def shell_size_Linf(r: int) -> int:
    return 1 if r == 0 else 8 * r


def shell_L1(r: int) -> Iterable[Point]:
    if r == 0:
        yield (0, 0)
        return
    for x in range(-r, r + 1):
        y = r - abs(x)
        yield (x, y)
        if y:
            yield (x, -y)


"""
geometry.py – spiral / shell utilities for Carry‑Symmetric Topology
------------------------------------------------------------------

Doctest sanity
--------------

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

Point = tuple[int, int]  # canonical lattice‑point type


# ──────────────────────────────────────────────────────────────────────────────
# Infinite generator of square‑spiral coordinates (clockwise)
# ──────────────────────────────────────────────────────────────────────────────
def _spiral_coords() -> Iterable[Point]:
    x = y = 0
    yield (0, 0)  # index 0
    step = 1
    while True:
        # → right
        for _ in range(step):
            x += 1
            yield (x, y)
        # ↑ up
        for _ in range(step):
            y += 1
            yield (x, y)
        step += 1
        # ← left
        for _ in range(step):
            x -= 1
            yield (x, y)
        # ↓ down
        for _ in range(step):
            y -= 1
            yield (x, y)
        step += 1


# ──────────────────────────────────────────────────────────────────────────────
# Index maps  (enumerative – fine for r ≤ 30 in tests)
# ──────────────────────────────────────────────────────────────────────────────
def spiral_index(pt: Point) -> int:
    """Return the spiral index of *pt* (O(index) enumeration; fine for tests)."""
    target_r = max(abs(pt[0]), abs(pt[1]))
    for idx, p in enumerate(_spiral_coords()):
        if p == pt:
            return idx
        if max(abs(p[0]), abs(p[1])) > target_r + 1:
            continue
    raise RuntimeError("Point not found (logic error)")


def inverse_index(n: int) -> Point:
    """Return lattice point at spiral position *n* (enumerative, but n ≤ 3 700)."""
    return next(islice(_spiral_coords(), n, None))


# ──────────────────────────────────────────────────────────────────────────────
# Shell generators
# ──────────────────────────────────────────────────────────────────────────────
def shell_Linf(r: int) -> Iterable[Point]:
    if r == 0:
        yield (0, 0)
        return
    k = r
    for y in range(-k + 1, k + 1):  # right edge
        yield (k, y)
    for x in range(k - 1, -k - 1, -1):  # top edge
        yield (x, k)
    for y in range(k - 1, -k - 1, -1):  # left edge
        yield (-k, y)
    for x in range(-k + 1, k):  # bottom edge
        yield (x, -k)


def shell_size_Linf(r: int) -> int:
    return 1 if r == 0 else 8 * r


def shell_L1(r: int) -> Iterable[Point]:
    if r == 0:
        yield (0, 0)
        return
    for x in range(-r, r + 1):
        y = r - abs(x)
        yield (x, y)
        if y:
            yield (x, -y)
