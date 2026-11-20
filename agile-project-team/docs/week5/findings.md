# Week 5 - Findings

Target: `week5/legacy_fees.py` (copied from the legacy invoice code in the lab handout).
No behaviour was changed until the characterization tests were in place and green.

## Findings table

| # | Smell | Where | Principle / rule |
|---|-------|-------|------------------|
| 1 | Long `if/elif` chain on `kind` | loop body and again after the loop | OCP - adding a student type means editing this function |
| 2 | Magic numbers: `1200`, `0.5`, `2000`, `5000` | fee calculation | Readability / single source of truth |
| 3 | One function calculates, formats, writes a file and prints | whole function | SRP - more than one reason to change |
| 4 | File opened without `with` and without `encoding=` | `open(...)` line | Resource safety (Pylint W1514 + R1732) |
| 5 | Fee worked out per course when only total hours matter | loop body | Needless repetition / efficiency |

## Extra smells

- `print(text)` couples the calculation to the console. Showing the invoice is the caller's job.
- The invoice line is built by string concatenation instead of an f-string.
- `int(total)` truncates any fractional amount silently (no rounding is documented).
- `make_invoice` has cyclomatic complexity 6 (Ruff C901 threshold 5).
- No validation of `kind`: an unknown value falls through every branch.

## Hidden bug

If `kind` is anything other than `regular`, `scholarship` or `international`, no branch runs. `total`
stays `0`, the code still writes `Invoice for <id>: 0 EGP` to disk, prints it and returns `0`. The caller
gets a normal-looking result and has no signal that the fee was never calculated. This is a silent
zero-fee invoice, not an exception.

The refactored code looks up `POLICIES[kind]`, so an unknown key raises `KeyError` immediately instead
of producing a believable but wrong result. This is the one intentional behaviour change; all three
valid kinds keep exactly the same totals (7200 / 3600 / 17000), which the characterization tests pin down.

## Refactoring moves (small steps, tests run after each)

1. Named the magic numbers (`FEE_PER_HOUR`, `RATE`, `SERVICE_FEE`).
2. Moved each fee rule into its own policy class with `fee(hours)` - SRP.
3. Replaced the `if/elif` chain with a `POLICIES` lookup - OCP.
4. Injected the writer (`writer=None`, default `FileWriter`) - DIP.
5. Removed `print` from the calculation and used `with open(..., encoding="utf-8")`.
