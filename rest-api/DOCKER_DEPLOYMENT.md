# Docker Deployment Guide for Task Manager API

## Overview

This guide explains how to deploy the Task Manager REST API using Docker and Docker Compose. The Docker configuration is optimized for both development and production environments.

## Docker Configuration Files

### 1. Dockerfile
- **Base Image**: Python 3.13-slim
- **Port**: 5000 (exposed and configured)
- **Health Check**: Built-in health monitoring
- **Optimized**: Multi-stage build with proper caching

### 2. docker-compose.yml
- **Service**: task-manager-api
- **Port Mapping**: 5000:5000
- **Volume**: Persistent data storage
- **Health Check**: Container health monitoring
- **Network**: Isolated network for security

### 3. .dockerignore
- **Optimized**: Excludes unnecessary files
- **Faster Builds**: Reduces build context size
- **Security**: Excludes sensitive files

## Quick Start

### Option 1: Using Docker Compose (Recommended)

```bash
# Build and start the service
docker-compose up --build

# Run in background
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop the service
docker-compose down
```

### Option 2: Using Docker Commands

```bash
# Build the image
docker build -t task-manager-api .

# Run the container
docker run -d \
  --name task-manager-api \
  -p 5000:5000 \
  -v $(pwd)/data:/app/data \
  task-manager-api

# View logs
docker logs -f task-manager-api

# Stop the container
docker stop task-manager-api
docker rm task-manager-api
```

## Docker Desktop Integration

### Why Docker Desktop Asks Questions

The original Dockerfile had issues that caused Docker Desktop to prompt for configuration:

1. **Variable Port**: Used `ARG FLASK_PORT` which wasn't properly resolved
2. **Missing Health Check**: No health monitoring
3. **Incomplete Environment**: Missing essential environment variables
4. **No Default Port**: Docker Desktop couldn't determine the port

### Fixed Configuration

The updated Dockerfile now includes:

```dockerfile
# Fixed port configuration
ENV FLASK_RUN_PORT=5000
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/api/docs/health || exit 1

# Complete environment setup
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONPATH=/app
```

## Deployment Methods

### 1. Docker Desktop GUI

1. **Build Image**:
   - Open Docker Desktop
   - Go to Images tab
   - Click "Build" or "Import"
   - Select the project directory
   - Tag: `task-manager-api`
   - Build context: Project root

2. **Run Container**:
   - Go to Containers tab
   - Click "Run"
   - Select the built image
   - Port: `5000:5000`
   - Name: `task-manager-api`
   - Click "Run"

3. **Access Application**:
   - Open browser to `http://localhost:5000`
   - API Documentation: `http://localhost:5000/api/docs`

### 2. Docker Compose (Recommended)

```bash
# Development
docker-compose up --build

# Production
docker-compose -f docker-compose.yml up -d --build
```

### 3. Command Line

```bash
# Build
docker build -t task-manager-api .

# Run with port mapping
docker run -d -p 5000:5000 --name task-manager-api task-manager-api

# Run with volume for data persistence
docker run -d \
  -p 5000:5000 \
  -v task-manager-data:/app/data \
  --name task-manager-api \
  task-manager-api
```

## Environment Configuration

### Development Environment

```bash
# Using docker-compose
docker-compose up --build

# Environment variables
FLASK_ENV=development
FLASK_DEBUG=true
```

### Production Environment

```bash
# Using docker-compose with production settings
docker-compose -f docker-compose.prod.yml up -d

# Environment variables
FLASK_ENV=production
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///data/tasks.db
```

## Volume Management

### Data Persistence

```bash
# Create named volume
docker volume create task-manager-data

# Run with volume
docker run -d \
  -p 5000:5000 \
  -v task-manager-data:/app/data \
  task-manager-api

# Backup data
docker run --rm \
  -v task-manager-data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/task-manager-backup.tar.gz /data
```

### Mount Host Directory

```bash
# Mount current directory data folder
docker run -d \
  -p 5000:5000 \
  -v $(pwd)/data:/app/data \
  task-manager-api
```

## Health Monitoring

### Health Check Endpoint

The container includes a built-in health check:

```bash
# Check container health
docker ps

# View health status
docker inspect task-manager-api | grep -A 10 Health

# Manual health check
curl http://localhost:5000/api/docs/health
```

### Health Check Response

```json
{
  "status": "healthy",
  "service": "Task Manager API Documentation",
  "openapi_spec_available": true,
  "endpoints": {
    "swagger_ui": "/api/docs",
    "openapi_yaml": "/api/docs/openapi.yaml",
    "openapi_json": "/api/docs/openapi.json"
  }
}
```

## Networking

### Default Network

```bash
# View networks
docker network ls

# Inspect network
docker network inspect task-manager-network
```

### Custom Network

```bash
# Create custom network
docker network create task-manager-net

# Run with custom network
docker run -d \
  --network task-manager-net \
  --name task-manager-api \
  -p 5000:5000 \
  task-manager-api
```

## Security Considerations

### Production Security

1. **Environment Variables**:
   ```bash
   # Set secure secret key
   docker run -d \
     -e SECRET_KEY=your-very-secure-secret-key \
     -p 5000:5000 \
     task-manager-api
   ```

2. **Non-root User** (Optional):
   ```dockerfile
   # Add to Dockerfile
   RUN adduser --disabled-password --gecos '' appuser
   USER appuser
   ```

3. **Read-only Filesystem**:
   ```bash
   # Run with read-only root filesystem
   docker run -d \
     --read-only \
     --tmpfs /tmp \
     -v task-manager-data:/app/data \
     task-manager-api
   ```

## Troubleshooting

### Common Issues

1. **Port Already in Use**:
   ```bash
   # Check what's using port 5000
   lsof -i :5000
   
   # Use different port
   docker run -d -p 8080:5000 task-manager-api
   ```

2. **Permission Issues**:
   ```bash
   # Fix volume permissions
   sudo chown -R $USER:$USER ./data
   ```

3. **Health Check Failures**:
   ```bash
   # Check logs
   docker logs task-manager-api
   
   # Test health endpoint manually
   curl http://localhost:5000/api/docs/health
   ```

### Debug Mode

```bash
# Run in debug mode
docker run -it --rm \
  -p 5000:5000 \
  -e FLASK_DEBUG=true \
  task-manager-api

# Interactive shell
docker run -it --rm \
  --entrypoint /bin/bash \
  task-manager-api
```

## Performance Optimization

### Resource Limits

```bash
# Set memory and CPU limits
docker run -d \
  --memory=512m \
  --cpus=1.0 \
  -p 5000:5000 \
  task-manager-api
```

### Multi-stage Build (Advanced)

```dockerfile
# Multi-stage build for smaller image
FROM python:3.13-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

## Monitoring and Logging

### Log Management

```bash
# View logs
docker logs -f task-manager-api

# Log rotation
docker run -d \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  task-manager-api
```

### Monitoring

```bash
# Resource usage
docker stats task-manager-api

# Container inspection
docker inspect task-manager-api
```

## Backup and Restore

### Database Backup

```bash
# Backup database
docker exec task-manager-api sqlite3 /app/data/tasks.db ".backup /app/data/backup.db"

# Copy backup from container
docker cp task-manager-api:/app/data/backup.db ./backup.db
```

### Complete Backup

```bash
# Backup entire data directory
docker run --rm \
  -v task-manager-data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/task-manager-backup.tar.gz /data
```

This Docker configuration ensures smooth deployment with Docker Desktop and provides production-ready features for reliable operation.
