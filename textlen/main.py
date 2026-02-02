import typer

app = typer.Typer()


@app.command()
def textlen(
    string: str,
    trim: bool = typer.Option(False, help="Trim leading and trailing whitespace"),
    count_bytes: bool = typer.Option(False, "--bytes", help="Count bytes instead of characters"),
) -> None:
    """Returns the length of a string"""
    if trim:
        string = string.strip()
    if count_bytes:
        string_len = len(string.encode('utf-8'))
        label = "Bytes"
    else:
        string_len = len(string)
        label = "Length"
    
    typer.echo(f"String: {string}")
    typer.secho(f"{label}: {string_len}", fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()
