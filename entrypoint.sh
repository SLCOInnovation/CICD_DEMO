#!/usr/bin/env bash
set -euo pipefail

# Render the template -> actual secrets file
envsubst < ./.streamlit/secrets.tmpl.toml > /app/.streamlit/secrets.toml

#uv sync after creating secrets file
uv sync

#lock permissions
chmod 600 /app/.streamlit/secrets.toml


exec "$@"