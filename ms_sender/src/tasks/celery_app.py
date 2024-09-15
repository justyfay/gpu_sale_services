from celery import Celery

from config import settings

celery: Celery = Celery(
    name="tasks",
    broker=settings.broker_url,
    backend="rpc://",
    include=["src.tasks.tasks"],
)

celery.conf.enable_utc = True
celery.conf.timezone = "UTC"
celery.conf.beat_schedule = {
    "update_products_from_rmq": {"task": "update_products_from_rmq", "schedule": 10}
}
