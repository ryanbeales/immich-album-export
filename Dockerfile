FROM ubuntu:24.10

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY .python-version /app/.python-version
# Install python
RUN uv python install $(cat /app/.python-version)

COPY uv.lock /app/uv.lock
COPY pyproject.toml /app/pyproject.toml
COPY logging.yaml /app/logging.yaml

# Sync proejct dependencies
RUN uv sync --frozen

# Copy the rest of the project into the image
ADD ./*.py /app

ENTRYPOINT ["uv", "run", "python", "main.py"]