#!/bin/env bash

uv run alembic revision --autogenerate
uv run alembic upgrade head

exec "$@"
