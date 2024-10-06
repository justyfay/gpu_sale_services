## Запуск сервиса и Celery для сбора задач
```
uvicorn ms_sender.main:app --host 0.0.0.0 --reload --port=8001
```
```
celery -A ms_sender.tasks.celery_app beat -l DEBUG
```
```
celery -A ms_sender.tasks.celery_app worker
```
```
celery -A ms_sender.tasks.celery_app flower
```
