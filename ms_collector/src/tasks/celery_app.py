from datetime import timedelta

from celery import Celery
from kombu import Queue, Exchange

from config import settings

celery: Celery = Celery(
    name="tasks",
    broker=settings.broker_url,
    include=["src.tasks.tasks"],
)
celery.conf.enable_utc = True
celery.conf.timezone = "UTC"

default_exchange_name = 'default'
default_queue_name = 'default'
default_routing_key = 'default'

product_events_queue_name = 'product_events'
product_events_routing_key = 'product_events'

default_exchange = Exchange(default_exchange_name, type='direct')

default_queue = Queue(
    default_queue_name,
    default_exchange,
    routing_key=default_routing_key
)

product_events = Queue(
    product_events_queue_name,
    default_exchange,
    routing_key=product_events_routing_key
)

celery.conf.task_queues = (default_queue, product_events)
celery.conf.task_default_exchange = default_exchange_name
celery.conf.task_default_queue = default_queue_name

celery.conf.task_routes = {
    'task_run': {
        'queue': default_queue_name
    },
}

celery.conf.beat_schedule = {
    "task_run": {
        "task": "task_run",
        "schedule": timedelta(minutes=10),
        "options": {"queue": default_queue}
    }
}
