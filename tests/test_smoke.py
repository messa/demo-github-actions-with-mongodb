"""Tests for hello_world MongoDB operations."""
import subprocess
import sys
from unittest.mock import MagicMock, patch

import pytest
from pymongo import MongoClient

from hello_world.main import sample_operations


def test_sample_operations():
    """Test sample_operations function directly with MongoDB."""
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client.test_db_pytest
    
    # Clean up before test
    db.test_collection.delete_many({})
    
    # Run sample_operations
    sample_operations(db)
    
    # Verify document was inserted
    found_doc = db.test_collection.find_one({"name": "Hello World"})
    assert found_doc is not None
    assert found_doc["name"] == "Hello World"
    assert found_doc["type"] == "demo"
    
    # Clean up after test
    db.test_collection.delete_many({})
    client.close()


def test_e2e_hello_world():
    """End-to-end test running the project via subprocess."""
    # Run the hello-world console script
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
