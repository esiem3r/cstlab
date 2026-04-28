# Carry-Symmetric Topology (`cstlab`) ![CI](https://github.com/esiem3r/cstlab/actions/workflows/ci.yml/badge.svg)

Reference implementation for Carry-Symmetric Topology lattice utilities.

```bash
pip install -e '.[dev]'
python -m pytest -q
python - <<'PY'
from cstlab.geometry import inverse_index, spiral_index

print(spiral_index((7, -3)))
print(inverse_index(spiral_index((7, -3))))
PY
```
