import asyncio

from src.services.update_products import UpdateProducts
from src.tasks.celery_app import celery as app


@app.task(name="update_products_from_rmq")
def update_products_from_rmq():
    asyncio.events.get_event_loop().run_until_complete(
        UpdateProducts().add_products_in_db()
    )
