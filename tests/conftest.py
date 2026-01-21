"""Pytest configuration and shared fixtures."""
import os

import pytest
from pymongo import MongoClient


@pytest.fixture
def mongo_client():
    """Fixture that provides a MongoDB client for testing."""
    mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
    client = MongoClient(
        mongodb_uri,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=5000,
        socketTimeoutMS=5000
    )
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
