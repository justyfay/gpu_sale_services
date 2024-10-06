from datetime import timedelta

from celery import Celery
from kombu import Exchange, Queue

from ms_collector.config import celery_settings

celery: Celery = Celery(
    name="tasks",
    broker=celery_settings.rmq_url,
    result_backend=celery_settings.redis_url,
    include=["ms_collector.tasks.tasks"],
)
celery.conf.enable_utc = True
celery.conf.timezone = "UTC"

default_exchange = Exchange(celery_settings.default_exchange_name, type="direct")

default_queue = Queue(
    name=celery_settings.default_queue_name,
    exchange=default_exchange,
    routing_key=celery_settings.default_routing_key,
)

product_events = Queue(
    name=celery_settings.product_events_queue_name,
    exchange=default_exchange,
    routing_key=celery_settings.product_events_routing_key,
)

celery.conf.task_queues = (default_queue, product_events)
celery.conf.task_default_exchange = celery_settings.default_exchange_name
celery.conf.task_default_queue = celery_settings.default_queue_name

celery.conf.task_routes = {
    "task_run": {"queue": celery_settings.default_queue_name},
}

celery.conf.beat_schedule = {
    "task_run": {"task": "task_run", "schedule": timedelta(minutes=10), "options": {"queue": default_queue}}
}
