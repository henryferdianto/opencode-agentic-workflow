# Agentic Development & Automated Data Engineering Workflow

![ci](https://github.com/henryferdianto/opencode-agentic-workflow/actions/workflows/ci.yml/badge.svg)

> **OpenCode terminal agents with MCP tools and reproducible AGENTS.md rules**

## Overview

A reference workflow that uses OpenCode terminal-based AI agents with custom tool-use configurations and Model Context Protocol (MCP) integrations to accelerate data pipeline development, automated refactoring and testing.

## Approach

1. **Repository context rules** (`AGENTS.md`) that encode coding standards.
2. **Custom agent tooling** configured through `opencode.json`.
3. **Automated data pipeline** scaffold that agents can extend and refactor.
4. **Quality gates**: linting, formatting and unit tests run before commit.

## Repository Structure

```
opencode-agentic-workflow/
├── AGENTS.md                 # agent context rules
├── opencode.example.json     # MCP + agent configuration
├── src/etl.py                # example data pipeline
├── tests/test_etl.py
├── requirements.txt
└── README.md
```

## Tech Stack

`OpenCode` · `MCP` · `Python` · `pytest` · `ruff`

## Getting Started

```bash
git clone https://github.com/henryferdianto/opencode-agentic-workflow.git
cd opencode-agentic-workflow
pip install -r requirements.txt
```

```bash
cp opencode.example.json opencode.json   # adjust model / MCP servers
opencode                                  # start the agent in this repo
pytest -q
```


<!-- completed -->

## Quickstart with Sample Data

The repository ships a synthetic data generator so the full pipeline can be run
without any private dataset:

```bash
make sample && python -m src.run_pipeline
```

## Tests

```bash
pip install -r requirements.txt
pytest -q
```

## Project Status

This repository contains the project documentation and a runnable reference
implementation. A synthetic data generator is included so every pipeline stage
can be executed end-to-end; replace the sample data with your own datasets in
`data/raw/` to reproduce real results.

## License

MIT License — see [LICENSE](LICENSE).


---

**Author:** Rifky Henry Ferdianto — Data Science undergraduate at ITERA  
GitHub: [@henryferdianto](https://github.com/henryferdianto) · Portfolio: [rifky-henry-ferdianto](https://github.com/henryferdianto/rifky-henry-ferdianto)
