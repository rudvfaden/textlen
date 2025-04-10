import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()


@app.command()
def textlen(string: str, trim: bool = typer.Option(
        False, help="Trim leading and trailing whitespace")) -> None:
    """Returns the length of a string

    Args:
        string (str): any string
        trim (bool): whether to trim whitespace
    """
    if trim:
        string = string.strip()
    length = str(len(string))
    table = Table("String", "Length")
    table.add_row(string, length)
    console.print(table)


if __name__ == "__main__":
    app()
