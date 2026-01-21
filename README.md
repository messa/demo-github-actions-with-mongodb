# demo-github-actions-with-mongodb
How to set up Github Actions workflows for Python projects using MongoDB

## Hello World Project

This repository contains a simple Python project that demonstrates MongoDB integration using the `uv` package manager.

### Project Structure

- `hello_world/` - Python package
  - `main.py` - Contains the main functions for MongoDB operations
    - `hello_world_main()` - Main entry point that connects to MongoDB
    - `sample_operations(db)` - Performs insert_one and find operations

### Requirements

- Python 3.12+
- MongoDB running on localhost:27017
- uv package manager

### Installation

1. Install uv (if not already installed):
   ```bash
   pip install uv
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

### Running the Project

To run the hello_world application:

```bash
uv run python -m hello_world.main
```

This will:
1. Connect to MongoDB at localhost:27017
2. Insert a document into the `test_collection`
3. Find and display the inserted document
4. Close the connection

### Development

The project uses `uv` for package management. To add new dependencies:

```bash
uv add <package-name>
```
