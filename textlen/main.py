import typer

app = typer.Typer()


@app.command()
def textlen(
    string: str,
    trim: bool = typer.Option(False, help="Trim leading and trailing whitespace"),
) -> None:
    """Returns the length of a string"""
    if trim:
        string = string.strip()
    typer.echo(f"String: {string}")
    typer.secho(f"Length: {len(string)}", fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()
