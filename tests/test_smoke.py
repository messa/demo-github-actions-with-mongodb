"""Tests for hello_world MongoDB operations."""
import os

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
