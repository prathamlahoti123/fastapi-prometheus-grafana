FROM ghcr.io/astral-sh/uv:python3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    PATH="/src/.venv/bin:$PATH"

WORKDIR /src

COPY ./pyproject.toml ./uv.lock ./

RUN apk add --no-cache curl && \
    uv sync --locked

COPY ./ ./

CMD ["uvicorn", "app.main:app",  "--host", "0.0.0.0"]
