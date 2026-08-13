# Textlen

A fast and simple Command Line Interface (CLI) tool to calculate the character length, byte count, or word count of a string. Built with Python, [Typer](https://typer.tiangolo.com/), and managed with [Poetry](https://python-poetry.org/).

## Features

- **Character Counting**: Get the character length of a string (default).
- **Byte Counting**: Count the UTF-8 bytes of a string (useful for multi-byte characters/emojis).
- **Word Counting**: Count the number of whitespace-separated words in a string.
- **Whitespace Trimming**: Trim leading and trailing whitespace before calculation.
- **Multiple Output Modes**: Run one or multiple calculations simultaneously (using `length`, `bytes`, `words`, or `all`).

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

If you have installed the package in editable mode or activated the virtual environment, you can run the CLI directly:

```bash
textlen "your string"
```

*Note: If the virtual environment is not activated, you can prepend `poetry run`:*
```bash
poetry run textlen "your string"
```

### Options

| Option | Short Flag | Description |
| :--- | :--- | :--- |
| `--trim` | `-t` | Trim leading and trailing whitespace. |
| `--mode` | `-m` | Metric(s) to calculate (`length`, `bytes`, `words`, `all`). Can be specified multiple times. Defaults to `length`. |
| `--help` | | Show the help message and exit. |

### Examples

#### 1. Basic Character Count
```bash
textlen "Camila"
```
Output:
```text
String: Camila
Length: 6
```

#### 2. Trim Whitespace
```bash
textlen "   hello world   " --trim
```
Output:
```text
String: hello world
Length: 11
```

#### 3. Count Bytes (UTF-8 support)
```bash
textlen "café" --mode bytes
```
Output:
```text
String: café
Bytes: 5
```

#### 4. Count Words
```bash
textlen "hello world from textlen" --mode words
```
Output:
```text
String: hello world from textlen
Words: 4
```

#### 5. Multiple Modes Simultaneously
```bash
textlen "test" --mode bytes --mode words
```
Output:
```text
String: test
Bytes: 4
Words: 1
```

#### 6. Calculate All Metrics
```bash
textlen "test" --mode all
```
Output:
```text
String: test
Length: 4
Bytes: 4
Words: 1
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
