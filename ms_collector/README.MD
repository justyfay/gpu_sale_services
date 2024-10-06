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
#####  Планировщик:
```
celery -A ms_collector.tasks.celery_app beat -l DEBUG
 ```
##### Worker
```
celery -A ms_collector.tasks.celery_app worker -Q default
```
##### Dashboard
```
celery -A ms_collector.tasks.celery_app flower
```
