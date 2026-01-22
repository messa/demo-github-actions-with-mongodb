# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install uv package manager using official installer
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy project files
COPY pyproject.toml uv.lock README.md ./
COPY hello_world ./hello_world

# Install dependencies
RUN uv sync --frozen --no-dev

# Set environment variable for MongoDB URI
# Default is localhost, but should be overridden when running in containers
# Example: docker run -e MONGODB_URI=mongodb://mongo:27017/ hello-world
ENV MONGODB_URI=mongodb://localhost:27017/

# Expose port (if needed for future services)
EXPOSE 8080

# Run the application
CMD ["uv", "run", "hello-world"]
