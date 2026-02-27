# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

`textlen` is a CLI tool that calculates the length, byte count, or word count of a string. Built with Typer and managed with Poetry.

## Commands

### Setup

```sh
poetry install
```

### Run the CLI

```sh
poetry run textlen "some string"
```

Or via `python -m textlen` if the virtualenv is activated.

### Run tests

```sh
poetry run pytest
```

Single test:

```sh
poetry run pytest tests/test_main.py::test_app
```

### Build distribution

```sh
poetry build
```

## Architecture

- **`textlen/main.py`** — Entire CLI logic lives here. A single Typer `app` with one command (`textlen`) that supports `--trim`, `--bytes`, and `--words` flags. The `main()` function is the console entry point.
- **`textlen/__main__.py`** — Enables `python -m textlen` invocation by delegating to `main()`.
- **`tests/test_main.py`** — Tests use Typer's `CliRunner` to invoke the app and assert on stdout output and exit codes.

## Conventions

- The CLI entry point is registered in `pyproject.toml` under `[tool.poetry.scripts]`.
- `--bytes` and `--words` are mutually exclusive; using both raises `typer.BadParameter`.
- Tests follow the pattern of invoking the Typer app via `CliRunner` and asserting on `result.stdout` and `result.exit_code`.
