## Запуск сервиса и Celery для сбора задач
```
uvicorn src.ms_sender.main:app --host 0.0.0.0 --reload --port=8001
```
```
celery -A src.ms_sender.tasks.celery_app beat -l DEBUG
```
```
celery -A src.ms_sender.tasks.celery_app worker
```
```
celery -A src.ms_sender.tasks.celery_app flower
```
