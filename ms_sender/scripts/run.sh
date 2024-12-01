#!/bin/bash

poetry run alembic upgrade head
poetry run gunicorn src.ms_sender.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8001