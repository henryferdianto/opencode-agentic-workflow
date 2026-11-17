# Agentic Development & Automated Data Engineering Workflow

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

## Project Status

This repository contains the project documentation and a runnable implementation
skeleton. Scripts are structured so that each pipeline stage can be executed and
extended independently. Update the configuration and data paths to run against
your own datasets.

## License

MIT License — see [LICENSE](LICENSE).


---

**Author:** Rifky Henry Ferdianto — Data Science undergraduate at ITERA  
GitHub: [@henryferdianto](https://github.com/henryferdianto) · Portfolio: [rifky-henry-ferdianto](https://github.com/henryferdianto/rifky-henry-ferdianto)
