"""Spiral and shell utilities for Carry-Symmetric Topology."""

from __future__ import annotations

from collections.abc import Iterator
from math import isqrt

Point = tuple[int, int]


def _check_nonnegative_radius(r: int) -> None:
    if r < 0:
        raise ValueError("radius must be nonnegative")


def shell_size_Linf(r: int) -> int:
    """Return the number of lattice points on the L-infinity shell of radius r."""
    _check_nonnegative_radius(r)
    return 1 if r == 0 else 8 * r


def shell_Linf(r: int) -> Iterator[Point]:
    """Yield the L-infinity shell in the same order used by the spiral index."""
    _check_nonnegative_radius(r)
    if r == 0:
        yield (0, 0)
        return

    for y in range(-r + 1, r + 1):
        yield (r, y)
    for x in range(r - 1, -r - 1, -1):
        yield (x, r)
    for y in range(r - 1, -r - 1, -1):
        yield (-r, y)
    for x in range(-r + 1, r + 1):
        yield (x, -r)


def shell_L1(r: int) -> Iterator[Point]:
    """Yield the L1 shell of radius r."""
    _check_nonnegative_radius(r)
    if r == 0:
        yield (0, 0)
        return

    for x in range(-r, r + 1):
        y = r - abs(x)
        yield (x, y)
        if y:
            yield (x, -y)


def spiral_index(pt: Point) -> int:
    """Return the clockwise square-spiral index of a lattice point."""
    x, y = pt
    r = max(abs(x), abs(y))
    if r == 0:
        return 0

    shell_start = (2 * r - 1) ** 2
    segment_len = 2 * r

    if x == r and y >= -r + 1:
        offset = y + r - 1
    elif y == r and x <= r - 1:
        offset = segment_len + (r - 1 - x)
    elif x == -r and y <= r - 1:
        offset = 2 * segment_len + (r - 1 - y)
    elif y == -r and x >= -r + 1:
        offset = 3 * segment_len + (x + r - 1)
    else:
        raise ValueError(f"{pt!r} is not on its inferred shell")

    return shell_start + offset


def inverse_index(n: int) -> Point:
    """Return the lattice point at clockwise square-spiral index n."""
    if n < 0:
        raise ValueError("index must be nonnegative")
    if n == 0:
        return (0, 0)

    r = (isqrt(n) + 1) // 2
    offset = n - (2 * r - 1) ** 2
    segment_len = 2 * r

    if offset < segment_len:
        return (r, -r + 1 + offset)
    if offset < 2 * segment_len:
        return (r - 1 - (offset - segment_len), r)
    if offset < 3 * segment_len:
        return (-r, r - 1 - (offset - 2 * segment_len))
    return (-r + 1 + (offset - 3 * segment_len), -r)
