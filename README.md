# Carry‑Symmetric Topology (`cstlab`) &nbsp; ![CI](https://github.com/esiem3r/cstlab/actions/workflows/ci.yml/badge.svg)

*Reference implementation + proofs for the Carry‑Symmetric Topology programme.*

```bash
pip install -e '.[dev]'              # editable install with dev tools
python -m pytest -q                  # run test‑suite
python - <<'PY'
from cstlab.geometry import spiral_index, inverse_index
print(spiral_index((7, -3)))         # demo
PY


MD
