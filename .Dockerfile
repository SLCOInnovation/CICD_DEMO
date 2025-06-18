# app/Dockerfile

FROM python:3.12-slim

# Install system dependencies
RUN pip install --no-cache-dir uv

# Copy dependency manifests for layer caching. Docker will cache the layers and use the cache unless changes are made to the layers.
WORKDIR /app
COPY pyproject.toml uv.lock ./

# Recreate locked environment inside the image
RUN uv sync --system --frozen

COPY . /app

# Container must listen to streamlit's default port
EXPOSE 8501

# Chech if the container is listening on the port
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health


CMD ["uv", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.headless=true", "--server.address=0.0.0.0"]

