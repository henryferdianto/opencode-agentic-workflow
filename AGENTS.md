# AGENTS.md

Repository-wide context for OpenCode agents.

## Conventions
- Python 3.11+, type hints on public functions.
- Every pipeline stage is a pure function in `src/`.
- Data never leaves `data/raw` unmodified; outputs go to `data/processed`.
- Add or update a test in `tests/` for every behaviour change.

## Commands
- Format: `ruff format .`
- Lint: `ruff check .`
- Test: `pytest -q`

## Guardrails
- Do not commit secrets or `.env` files.
- Do not delete data files; write new ones instead.
