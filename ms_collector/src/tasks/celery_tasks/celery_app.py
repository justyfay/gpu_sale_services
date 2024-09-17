from celery import Celery

from config import settings

celery: Celery = Celery(
    name="tasks",
    broker=settings.broker_url,
    backend="rpc://",
    include=["src.tasks.celery_tasks.tasks"],
)

celery.conf.enable_utc = True
celery.conf.timezone = "UTC"
celery.conf.beat_schedule = {
    "send_products_from_collector": {
        "task": "send_products_from_collector",
        "schedule": 600,
    }
}
