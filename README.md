# demo-github-actions-with-mongodb
How to set up Github Actions workflows for Python projects using MongoDB

## Hello World Project

This repository contains a simple Python project that demonstrates MongoDB integration using the `uv` package manager.

### Project Structure

- `hello_world/` - Python package
  - `main.py` - Contains the main functions for MongoDB operations
    - `hello_world_main()` - Main entry point that connects to MongoDB
    - `sample_operations(db)` - Performs insert_one and find operations
- `tests/` - Test suite
  - `test_smoke.py` - Contains pytest tests for MongoDB operations

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

Or using the console script:

```bash
uv run hello-world
```

This will:
1. Connect to MongoDB at localhost:27017
2. Insert a document into the `test_collection`
3. Find and display the inserted document
4. Close the connection

### Testing

The project includes pytest tests that verify MongoDB operations.

#### Prerequisites for Testing

Make sure MongoDB is running on localhost:27017 before running tests:

```bash
# On systems with systemd (Ubuntu/Debian)
sudo systemctl start mongodb

# On macOS with Homebrew
brew services start mongodb-community

# Or run MongoDB in Docker
docker run -d -p 27017:27017 mongo:7
```

#### Running Tests Locally

To run all tests:

```bash
uv run pytest -v tests
```

To run specific tests:

```bash
# Run only the direct function test
uv run pytest -v tests/test_smoke.py::test_sample_operations

# Run only the e2e test
uv run pytest -v tests/test_smoke.py::test_e2e_hello_world
```

#### Test Description

- **test_sample_operations** - Directly tests the `sample_operations()` function by calling it with a test database and verifying the MongoDB operations
- **test_e2e_hello_world** - End-to-end test that runs the entire application via subprocess and verifies the output

#### GitHub Actions

Tests run automatically in GitHub Actions on push and pull requests. The workflow is configured to:
- Test against Python 3.11, 3.13, and 3.14
- Use MongoDB 7 service container
- Run all pytest tests

### Development

The project uses `uv` for package management. To add new dependencies:

```bash
uv add <package-name>
```
