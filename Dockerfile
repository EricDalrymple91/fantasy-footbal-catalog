FROM python:3.13-slim

EXPOSE 8080
ENV PATH=/ff/.venv/bin:/usr/local/bin:$PATH
ENV PYTHONPATH=/ff
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y \
        curl \
        gdal-bin \
        postgresql-client \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

RUN mkdir -p /ff

WORKDIR /ff

COPY manage.py pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv venv && \
    uv sync --frozen --all-extras

COPY ./ /ff

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --all-extras

CMD ["/bin/bash"]
