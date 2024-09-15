# Локальный запуск (MAC OS, Apple Silicon)
## 1. Предварительные настройки
- Установить postgres, инициализировать БД и запустить.
```
pg_ctl -D /opt/homebrew/var/services@16 initdb
```
```
pg_ctl -D /opt/homebrew/var/services@16 -U potgres -o "-F -p 5434" start
```
- Установить и запустить RabbitMQ
```
brew install rabbitmq
```
```
brew services start rabbitmq
```
## 2. Запуск сервиса
Следующие команды запустят периодическую отправку данных по товарам в RMQ (включая предварительный сбор/обновление данных).
### С помощью taskiq
Рабочий вариант, будет отправлять по таймингу сообщения в указанную очередь.
#####  FastStream (запустить для создания очереди и обменника):
```
faststream run src.tasks.fast_stream:app
```
#####  Планировщик:
```
taskiq scheduler src.tasks.fast_stream:scheduler
```
### С помощью celery
Не очень рабочий вариант. Будет отправлять сообщения, но каждый раз названием очереди выступает рандомный uuid.
```
celery -A src.tasks.celery_tasks.celery_app beat -l DEBUG
```
```
celery -A src.tasks.celery_tasks.celery_app worker
```
```
celery -A src.tasks.celery_tasks.celery_app flower
```