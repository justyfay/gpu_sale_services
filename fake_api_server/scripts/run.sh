#!/bin/bash

poetry run gunicorn src.fake_api_server.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000