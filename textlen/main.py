import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()


@app.command()
def textlen(string: str):
    """Returns the length of a string

    Args:
        string (str): any string
    """
    lenght = str(len(string))
    table = Table("String", "Length")
    table.add_row(string, lenght)
    console.print(table)


if __name__ == "__main__":
    app()
