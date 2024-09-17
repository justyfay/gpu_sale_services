from celery import Celery
from kombu import Queue, Exchange

from config import settings

celery: Celery = Celery(
    name="tasks",
    broker=settings.broker_url,
    backend="rpc://",
    include=["src.tasks.celery_tasks.tasks"],
)
celery.conf.task_queues = (
    Queue("product_events", Exchange("product_events"), routing_key='product_events', auto_delete=False),
)
celery.conf.task_routes = {
    'send_products_from_collector': {
        'queue': 'product_events',
    },
}
celery.conf.enable_utc = True
celery.conf.timezone = "UTC"
celery.conf.beat_schedule = {
    "send_products_from_collector": {
        "task": "send_products_from_collector",
        "schedule": 30,
    }
}
