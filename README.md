# Textlen

A fast and simple Command Line Interface (CLI) tool to calculate the character length, byte count, or word count of a string. Built with Python, [Typer](https://typer.tiangolo.com/), and managed with [Poetry](https://python-poetry.org/).

## Features

- **Character Counting**: Get the character length of a string (default).
- **Byte Counting**: Count the UTF-8 bytes of a string (useful for multi-byte characters/emojis).
- **Word Counting**: Count the number of whitespace-separated words in a string.
- **Whitespace Trimming**: Trim leading and trailing whitespace before calculation.
- **Mutually Exclusive Options**: Ensures clean command logic (e.g. `--bytes` and `--words` cannot be combined).

## Installation

Ensure you have Python 3.9+ installed.

### Using Poetry

1. Clone this repository:
   ```bash
   git clone https://github.com/rudvfaden/textlen.git
   cd textlen
   ```

2. Install the dependencies:
   ```bash
   poetry install
   ```

## Usage

You can run the CLI via Poetry:

```bash
poetry run textlen "your string"
```

### Options

| Option | Short Flag | Description |
| :--- | :--- | :--- |
| `--trim` | `-t` | Trim leading and trailing whitespace. |
| `--mode` | `-m` | Metric to calculate (`length`, `bytes`, `words`). Defaults to `length`. |
| `--help` | | Show the help message and exit. |

### Examples

#### 1. Basic Character Count
```bash
poetry run textlen "Camila"
```
Output:
```text
String: Camila
Length: 6
```

#### 2. Trim Whitespace
```bash
poetry run textlen "   hello world   " --trim
```
Output:
```text
String: hello world
Length: 11
```

#### 3. Count Bytes (UTF-8 support)
```bash
poetry run textlen "café" --mode bytes
```
Output:
```text
String: café
Bytes: 5
```

#### 4. Count Words
```bash
poetry run textlen "hello world from textlen" --mode words
```
Output:
```text
String: hello world from textlen
Words: 4
```

## Development

### Running Tests

We use `pytest` for unit testing. You can run all tests with:

```bash
poetry run pytest
```

### Project Structure

- [`textlen/main.py`](file:///Users/rudfaden/Documents/textlen/textlen/main.py): Main entry point and CLI command logic.
- [`tests/test_main.py`](file:///Users/rudfaden/Documents/textlen/tests/test_main.py): Test suites checking various options and validation rules.
