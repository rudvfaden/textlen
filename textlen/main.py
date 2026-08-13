import typer

app = typer.Typer(add_completion=True)


@app.command()
def textlen(
    string: str,
    trim: bool = typer.Option(
        False, "--trim", "-t", help="Trim leading and trailing whitespace"),
    count_bytes: bool = typer.Option(
        False, "--bytes", "-b", help="Count bytes instead of characters"),
    count_words: bool = typer.Option(
        False, "--words", "-w", help="Count words instead of characters")
) -> None:
    """Returns the length of a string"""
    if trim:
        string = string.strip()

    if count_bytes and count_words:
        raise typer.BadParameter("Cannot use --bytes and --words together")
    elif count_bytes:
        string_len = len(string.encode('utf-8'))
        label = "Bytes"
    elif count_words:
        string_len = len(string.split())
        label = "Words"
    else:
        string_len = len(string)
        label = "Length"

    typer.echo(f"String: {string}")
    typer.secho(f"{label}: {string_len}", fg=typer.colors.GREEN)


def main():
    """Console entry point for packaging / installers."""
    app()


if __name__ == "__main__":
    main()
