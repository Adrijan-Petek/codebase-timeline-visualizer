# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY backend/src/ ./backend/src/
COPY cli/src/ ./cli/src/
COPY setup.py .

# Install the package
RUN pip install -e .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expose port for web interface
EXPOSE 3001

# Set environment variables
ENV PYTHONPATH=/app
ENV FLASK_APP=cli.src.main

# Default command
CMD ["python", "-m", "cli.src.main", "serve", "--port", "3001"]