from typer.testing import CliRunner

from textlen.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code == 0
    assert "6" in result.stdout
    assert "Camila" in result.stdout

def test_bytes_option():
    """Test byte counting with --bytes flag"""
    # ASCII characters: 1 byte each
    result = runner.invoke(app, ["hello", "--bytes"])
    assert result.exit_code == 0
    assert "Bytes: 5" in result.stdout
    
    # UTF-8 emoji: multi-byte characters
    result = runner.invoke(app, ["café", "--bytes"])
    assert result.exit_code == 0
    assert "Bytes: 5" in result.stdout  # c=1, a=1, f=1, é=2 bytes
    
    # Without --bytes flag (character count)
    result = runner.invoke(app, ["café"])
    assert result.exit_code == 0
    assert "Length: 4" in result.stdout  # 4 characters