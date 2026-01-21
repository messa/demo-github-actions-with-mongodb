"""Main module with MongoDB integration."""
from pymongo import MongoClient


def sample_operations(db):
    """Perform sample MongoDB operations.
    
    Args:
        db: MongoDB database instance
    """
    # Insert a document
    collection = db.test_collection
    result = collection.insert_one({"name": "Hello World", "type": "demo"})
    print(f"Inserted document with ID: {result.inserted_id}")
    
    # Find the document
    found_doc = collection.find_one({"name": "Hello World"})
    print(f"Found document: {found_doc}")


def hello_world_main():
    """Main function that connects to MongoDB and performs operations."""
    # Connect to MongoDB (default localhost:27017)
    client = MongoClient("mongodb://localhost:27017/")
    
    # Use a test database
    db = client.hello_world_db
    
    # Call sample_operations
    sample_operations(db)
    
    # Close the connection
    client.close()
    print("MongoDB operations completed successfully!")


if __name__ == "__main__":
    hello_world_main()
