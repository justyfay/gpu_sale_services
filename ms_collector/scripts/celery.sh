#!/bin/bash

if [[ "${1}" == "celery" ]]; then
    poetry run celery --app=src.ms_collector.tasks.celery_app:celery worker -Q default -l INFO; fi
if [[ "${1}" == "celery_beat" ]]; then
    poetry run celery --app=src.ms_collector.tasks.celery_app:celery beat -l DEBUG;
elif [[ "${1}" == "flower" ]]; then
    poetry run celery --app=src.ms_collector.tasks.celery_app:celery flower; fi