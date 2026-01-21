"""Tests for hello_world MongoDB operations."""
from hello_world.main import sample_operations


def test_sample_operations(test_db):
    """Test sample_operations function directly with MongoDB."""
    # Run sample_operations
    sample_operations(test_db)
    
    # Verify document was inserted
    found_doc = test_db.test_collection.find_one({"name": "Hello World"})
    assert found_doc is not None
    assert found_doc["name"] == "Hello World"
    assert found_doc["type"] == "demo"
