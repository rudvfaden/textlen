from typer.testing import CliRunner

from textlen.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code == 0
    assert "6" in result.stdout
    assert "Camila" in result.stdout

def test_bytes_option():
    """Test byte counting with --mode bytes option"""
    # ASCII characters: 1 byte each
    result = runner.invoke(app, ["hello", "--mode", "bytes"])
    assert result.exit_code == 0
    assert "Bytes: 5" in result.stdout
    
    # UTF-8 emoji: multi-byte characters
    result = runner.invoke(app, ["café", "--mode", "bytes"])
    assert result.exit_code == 0
    assert "Bytes: 5" in result.stdout  # c=1, a=1, f=1, é=2 bytes
    
    # Without --mode option (default to length)
    result = runner.invoke(app, ["café"])
    assert result.exit_code == 0
    assert "Length: 4" in result.stdout  # 4 characters
    
def test_trim_option():
    """Test trimming whitespace with --trim flag"""
    input_string = "   hello world   "
    
    # Without trim
    result = runner.invoke(app, [input_string])
    assert result.exit_code == 0
    assert "Length: 17" in result.stdout  # includes spaces
    
    # With trim
    result = runner.invoke(app, [input_string, "--trim"])
    assert result.exit_code == 0
    assert "Length: 11" in result.stdout  # trimmed spaces
    
def test_words_option():
    """Test word counting with --mode words option"""
    input_string = "hello world from textlen"
    
    # With --mode words
    result = runner.invoke(app, [input_string, "--mode", "words"])
    assert result.exit_code == 0
    assert "Words: 4" in result.stdout  # 4 words
    
    # Without --mode option (default to length)
    result = runner.invoke(app, [input_string])
    assert result.exit_code == 0
    assert "Length: 24" in result.stdout  # includes spaces

def test_invalid_mode_option():
    """Test that an invalid mode is rejected by Typer"""
    result = runner.invoke(app, ["hello", "--mode", "invalid_value"])
    assert result.exit_code != 0
    assert "Invalid value for '--mode'" in result.stdout or "Error" in result.stdout