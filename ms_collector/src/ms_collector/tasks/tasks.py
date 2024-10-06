import asyncio

from celery.utils import worker_direct

from ms_collector.services.construct_data import ConstructData
from ms_collector.tasks.celery_app import celery as app
from ms_collector.tasks.celery_app import product_events


@app.task(name="task_run")
def task_run():  # noqa ANN001
    return send_products_from_collector.apply_async(
        args=(asyncio.events.get_event_loop().run_until_complete(ConstructData.construct_product_data()),),
        queue=worker_direct(product_events),
    )


@app.task(name="send_products_from_collector")
def send_products_from_collector(func):  # noqa ANN001
    return func
