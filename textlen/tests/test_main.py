from typer.testing import CliRunner

from textlen.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code == 0
    assert "6" in result.stdout
    assert "Camila" in result.stdout
