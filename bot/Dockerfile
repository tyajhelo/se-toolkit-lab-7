FROM harbor.pg.innopolis.university/docker-hub-cache/astral/uv:python3.14-bookworm-slim AS builder

WORKDIR /app

COPY bot/pyproject.toml /app/bot/pyproject.toml
COPY bot /app/bot

RUN --mount=type=cache,target=/root/.cache/uv \
    cd /app/bot && uv sync

FROM harbor.pg.innopolis.university/docker-hub-cache/python:3.14.2-slim-bookworm

RUN groupadd --system --gid 999 nonroot \
    && useradd --system --gid 999 --uid 999 --create-home nonroot

COPY --from=builder --chown=nonroot:nonroot /app /app

WORKDIR /app/bot
ENV PYTHONUNBUFFERED=1
USER nonroot

CMD ["/app/bot/.venv/bin/python", "bot.py"]
