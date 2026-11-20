# Week 5 - After Refactoring

All figures below were measured on Python 3.12 with ruff 0.17.6, pylint 4.1.4 and pytest 9.2.0.

## Before / after

| Measure | Before (`legacy_fees.py`) | After (`fees.py`) |
|---|---|---|
| Cyclomatic complexity of `make_invoice` (Ruff C901) | 6 | 1 |
| Pylint score | 7.78/10 | 10.00/10 |
| Ruff checks on the active code | 1 error (C901) | 0 errors |
| Tests passing | 5 (grades kata only) | 10 (5 grades + 5 fees) |
| Coverage of `fees.py` | not measured | 100% (23/23 statements) |
| Add a new student type | edit the `if/elif` chain twice | add one policy class + one dict entry |
| Test without writing files | not possible | yes, with `FakeWriter` |
| Unknown `kind` | silent 0 EGP invoice | `KeyError` (visible failure) |

The original `legacy_fees.py` is kept only as the before snapshot and is ignored by Ruff for C901 in
`week5/pyproject.toml`; it is not part of the shipped module.

## Pairing reflection

We drove the grades kata one test at a time and kept a commit for each red-green cycle, which made it
obvious when a test had been written before the code. Before touching the fees module we captured its
current behaviour with characterization tests, so every small move could be checked against a known
baseline. Rotating driver and navigator meant the `if/elif` chain and the hidden zero-fee bug were
spotted by the person who was not typing. The final design puts each fee rule in its own policy class
and injects the writer, so a new type is one class and one dictionary entry instead of another edit to
`make_invoice`.
