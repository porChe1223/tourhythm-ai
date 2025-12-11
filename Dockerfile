FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

# Copy dependency files
COPY ./requirements.txt /code/requirements.txt
COPY ./pyproject.toml /code/pyproject.toml

# Install dependencies
RUN /bin/uv pip install --system --no-cache-dir -r /code/requirements.txt

# Copy application
COPY src /code/src

# Install application
RUN /bin/uv pip install --system -e .

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "9000"]
