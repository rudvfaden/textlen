from enum import Enum
import typer

app = typer.Typer(add_completion=True)


class MetricMode(str, Enum):
    length = "length"
    bytes = "bytes"
    words = "words"


TRIM_OPTION = typer.Option(
    False, "--trim", "-t", help="Trim leading and trailing whitespace"
)
MODE_OPTION = typer.Option(
    MetricMode.length, "--mode", "-m", help="Metric to calculate"
)


@app.command()
def textlen(
    string: str,
    trim: bool = TRIM_OPTION,
    mode: MetricMode = MODE_OPTION,
) -> None:
    """Returns the length of a string"""
    if trim:
        string = string.strip()

    # Dispatch dictionary mapping Enums to calculation functions
    dispatch = {
        MetricMode.length: lambda s: ("Length", len(s)),
        MetricMode.bytes: lambda s: ("Bytes", len(s.encode("utf-8"))),
        MetricMode.words: lambda s: ("Words", len(s.split())),
    }

    # Fetch and execute the correct calculator with zero if-else checks
    label, val = dispatch[mode](string)

    typer.echo(f"String: {string}")
    typer.secho(f"{label}: {val}", fg=typer.colors.GREEN)


def main():
    """Console entry point for packaging / installers."""
    app()


if __name__ == "__main__":
    main()
