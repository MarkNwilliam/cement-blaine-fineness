<div align="center">

# Cement Fineness — Blaine Air Permeability Calculator

**Specific surface area of cement by the Blaine method (ASTM C204 / EN 196-6)**

The number a cement plant QC lab reports on every batch — and you can run in
your browser or from the command line.

[![Web UI](https://img.shields.io/badge/web%20UI-standalone-f59e0b)](#)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](#)
[![No deps](https://img.shields.io/badge/dependencies-none-blue)](#)
[![Tests](https://img.shields.io/badge/tests-5%20passing-green)](#)
[![License](https://img.shields.io/badge/license-MIT-green)](#)

</div>

---

## Why this exists

Blaine fineness controls how fast cement hydrates and how much early strength
it delivers. The same permeability time can mean different fineness depending
on bed geometry and sample density, so labs calibrate against a reference
sample. This tool does that calibration correctly — no more squinting at a
table — and gives the direct-from-geometry route as a fallback.

## The method

Air is drawn through a compacted bed of cement of known volume. The time taken
for a fixed quantity of air to pass, combined with the bed porosity and density,
gives the specific surface area. Two routes are supported:

**1. Reference-sample calibration (recommended)**
```
S = Ss x ( t x Ks ) / ( ts x K )
```
`Ss` = reference Blaine surface · `t`/`ts` = sample/reference times ·
`K`/`Ks` = bed K constants.

**2. Direct from bed geometry and viscosity**
```
S = (1/rho) x sqrt( eta x t / eps^3 ) x F
```
`rho` = density · `eta` = air viscosity · `eps` = porosity · `t` = time ·
`F` = apparatus constant.

## Features

- Two calculation routes with live recalculation as you type
- Gradient-of-quality guidance (very high / high / mid / low fineness bands)
- A `blaine.py` CLI that mirrors the same math for automated QC scripts
- A unit-tested core (`test_blaine.py`, 5 passing)

## Quick start

```bash
# web UI
open index.html            # or: python3 -m http.server 8000

# CLI
python3 blaine.py --ref 3200 --ref-time 45 --time 52 --density 3.15
# -> Blaine surface (reference method): 3,698 cm2/g

# tests
python3 -m unittest test_blaine -v
```

## Repository layout

```
cement-blaine-fineness/
├── index.html       # interactive calculator
├── blaine.py        # CLI / library implementation
├── test_blaine.py   # unit tests
└── README.md
```

## License

MIT.
