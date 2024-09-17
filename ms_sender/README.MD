
## Запуск сервиса и Celery для сбора задач
```
uvicorn src.main:app --host 0.0.0.0 --reload --port=8001
```
```
celery -A src.tasks.celery_app beat -l DEBUG
```
```
celery -A src.tasks.celery_app worker
```
```
celery -A src.tasks.celery_app flower
```