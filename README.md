# Low-Level Design Practice

A small Python workspace for studying object-oriented design, design patterns, and
classic low-level design interview problems.

## Layout

```text
src/
├── common/           # Shared value objects, interfaces, and helpers
├── design_patterns/  # One focused implementation per pattern
└── problems/         # Interview-style designs, one problem per module/package
tests/                # Mirrors src/lld_practice/
```

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Suggested workflow

For each exercise:

1. Write the requirements and assumptions in the module docstring.
2. Model the core entities and their responsibilities.
3. Add a small, focused implementation.
4. Capture behavior and edge cases in `tests/`.
5. Note trade-offs and possible extensions in the exercise README or docstring.

The starter `common.hello_world` module is only a smoke test for the project wiring. Replace
it with the first design exercise when you are ready.

