# app/Dockerfile

FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends gettext-base \
    && rm -rf /var/lib/apt/lists/*

# Install system dependencies
RUN pip install --no-cache-dir uv

# Copy dependency manifests for layer caching. Docker will cache the layers and use the cache unless changes are made to the layers.
WORKDIR /app
COPY pyproject.toml uv.lock ./

# Recreate locked environment inside the image
RUN uv sync --frozen

COPY . /app

# Container must listen to streamlit's default port
EXPOSE 8501

# Chech if the container is listening on the port
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

WORKDIR /app

CMD ["uv", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.headless=true", "--server.address=0.0.0.0"]

