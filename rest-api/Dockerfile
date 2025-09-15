FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies (curl only; no compiler needed)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create data directory for database
RUN mkdir -p /app/data

# Set environment variables
ENV PYTHONPATH=/app

# Expose port
EXPOSE 8500

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8500/api/docs/health || exit 1

# Run the application
CMD ["python", "app.py"]