"""End-to-end tests for hello_world application."""
import subprocess
import sys


def test_e2e_hello_world():
    """End-to-end test running the application via subprocess."""
    # Run the application as a module
    result = subprocess.run(
        [sys.executable, "-m", "hello_world.main"],
        capture_output=True,
        text=True,
        timeout=10
    )
    # Check that the command executed successfully
    assert result.returncode == 0, f"Process failed with stderr: {result.stderr}"
    
    # Verify expected output
    assert "Inserted document with ID:" in result.stdout
    assert "Found document:" in result.stdout
    assert "MongoDB operations completed successfully!" in result.stdout
