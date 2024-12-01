from celery import Celery

from src.ms_sender.config import settings

celery: Celery = Celery(
    name="tasks",
    broker=settings.rmq_url,
    backend=settings.redis_url,
    include=["src.ms_sender.tasks.tasks"],
)

celery.conf.enable_utc = True
celery.conf.timezone = "UTC"
celery.conf.beat_schedule = {
    "update_products_from_rmq": {"task": "update_products_from_rmq", "schedule": 10}
}
