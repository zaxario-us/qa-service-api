FROM python:3.13.9-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./src .
COPY ./pyproject.toml .

RUN pip install uv
RUN uv sync

RUN uv run alembic init migrations
COPY ./src/env.py ./migrations

RUN chmod +x prestart.sh

ENTRYPOINT ["./prestart.sh"]
CMD ["uv", "run", "main.py"]
