"""Tests for hello_world MongoDB operations."""
import os
import subprocess
import sys

import pytest
from pymongo import MongoClient

from hello_world.main import sample_operations


@pytest.fixture
def mongo_client():
    """Fixture that provides a MongoDB client for testing."""
    mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
    client = MongoClient(mongodb_uri)
    yield client
    client.close()


@pytest.fixture
def test_db(mongo_client):
    """Fixture that provides a clean test database."""
    db = mongo_client.test_db_pytest
    # Clean up before test
    db.test_collection.delete_many({})
    yield db
    # Clean up after test
    db.test_collection.delete_many({})


def test_sample_operations(test_db):
    """Test sample_operations function directly with MongoDB."""
    # Run sample_operations
    sample_operations(test_db)
    
    # Verify document was inserted
    found_doc = test_db.test_collection.find_one({"name": "Hello World"})
    assert found_doc is not None
    assert found_doc["name"] == "Hello World"
    assert found_doc["type"] == "demo"


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
